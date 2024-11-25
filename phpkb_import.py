import mysql.connector
from sshtunnel import SSHTunnelForwarder
from getpass import getpass
import html
from html.parser import HTMLParser
import bs4
from markdownify import markdownify as md
from markdownify import MarkdownConverter
import re
from pathvalidate import sanitize_filename
from pathlib import Path
import shutil
from cryptography.fernet import Fernet
import os
import os.path
import json
from sshtunnel import SSHTunnelForwarder

KB_ID_TO_FILENAME_MAP = None
KB_ID_TO_TITLE_MAP = None
KB_ID_TO_TITLE_MAP_FILE = '.article_id_filename_map_v5.json'
THIS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))
IMPORT_PATH_DEFAULT = 'phpkb_content'
importPath = input(f'Path to import (default `{IMPORT_PATH_DEFAULT}`): ') 
KB_DIR = os.path.dirname(importPath) if importPath else IMPORT_PATH_DEFAULT
TOTAL_PAGES_IMPORTED = 0
CONNECTION = None
DOCS_RU_FOLDER = 'docs/ru'
HYPERLINKS_FILE = os.path.join(DOCS_RU_FOLDER, '.snippets/hyperlinks_mkdocs_to_kb_map.md')

# Function to search for pattern in hyperlinks file and replace
def find_url_in_snippet(article_id, anchor):
    with open(HYPERLINKS_FILE, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    url = ''
    for line in lines:
        # Search for the url with articleId
        match = None
        if anchor:
            match = re.search(fr'(\[.*?\]):.*kbArticleURLPrefix.*{article_id}#{anchor}\n', line)
        #     print (f"articleId {article_id} and anchor {anchor}")
        if not match:
            match = re.search(fr'(\[.*?\]):.*kbArticleURLPrefix.*{article_id}\n', line)
        if match and match.group(1):
            url = match.group(1)
            #print(f"Found link and URL for articleId {article_id}: {url}")
    return url

def importCategoryChildren(parent, categoryDirectory):
        id = parent[0]
        title = parent[1]
        c4 = CONNECTION.cursor()    
        c4.execute("""
            SELECT DISTINCT (category_id), category_name, parent_id
            FROM phpkb_categories 
            WHERE category_show='yes' 
            AND category_status = 'private'
            AND phpkb_categories.language_id = 2
            AND parent_id = {}
            """.format(id))
        children = c4.fetchall()
        print("\n-----\n\nCategory {}. {}. Children: {}\n".format(id, title, children))
        dirName = sanitize_filename('{}. {}'.format(id, str(title)))
        categoryDir = os.path.join(categoryDirectory, dirName)
        if os.path.exists(categoryDir): 
            print('Deleting dir:' + categoryDir)
            shutil.rmtree(categoryDir, ignore_errors=True)
        Path(categoryDir).mkdir(parents=True, exist_ok=True)
        print('Importing articles to dir: ' + categoryDir + '\n')
        importArtciclesInCategory(id, categoryDir)
        for child in children:
            importCategoryChildren(child, categoryDir)
        return children
    
        
def importArtciclesInCategory (categoryId, categoryDir):
    c = CONNECTION.cursor()
    c.execute(f"""
            SELECT DISTINCT (phpkb_articles.article_id), phpkb_articles.article_content, phpkb_articles.article_title 
            FROM phpkb_articles, phpkb_relations, phpkb_categories 
            WHERE article_show='yes' 
            AND phpkb_relations.category_id = {categoryId} 
            AND phpkb_relations.article_id = phpkb_articles.article_id
            """)
    
    articles = c.fetchall()
    global TOTAL_PAGES_IMPORTED
    pages = 0
    for id, content, title in articles:
     
        sanitizedTitle = sanitize_filename(str(title))
        existingFilename = findFilenameByArticleId(id, DOCS_RU_FOLDER)
        if existingFilename:
            sanitizedTitle = existingFilename
        else: updateMappingJson(id, sanitizedTitle, KB_ID_TO_TITLE_MAP, KB_ID_TO_TITLE_MAP_FILE)
        filename = os.path.join(categoryDir, f"{id}-{sanitizedTitle}.md")
        filename_html = os.path.join(categoryDir, f"{id}-{sanitizedTitle}.html")
        print ('    Importing article: ' + filename)
        
        with open(filename, "w+") as b:
            
            p = bs4.BeautifulSoup(html.unescape(content), 'html.parser')
            article_title = p.new_tag("h1")
            article_title.string=title
            p.insert(0, article_title)
            with open(filename_html, "w+") as html_file:
                html_file.write(str(p))    
            markdown = MarkdownConverter(heading_style='ATX', bullets='-', escape_misc=False).convert_soup(p)
            # Remove redundant new lines
            pattern = re.compile(r'^\n^\n\n*', flags=re.MULTILINE)
            markdown = re.sub(pattern, r'\n', markdown)
            # Remove redundant spaces before new lines
            pattern = re.compile(r' +\n', flags=re.MULTILINE)
            markdown = re.sub(pattern, r'\n', markdown)
            # Remove redundant TOC
            pattern = re.compile(r'(#+ +|\*\* ?)Содержание.*\n*((( {0,4}|\t*)(\d\.|-).*\n+)*\n* {0,4})*\n', flags=re.MULTILINE)
            markdown = re.sub(pattern, r'', markdown)
            # Remove redundant [*‌* К началу](#) links
            pattern = re.compile(r'^.*\[.*К началу\]\(#\).*$', flags=re.MULTILINE)
            markdown = re.sub(pattern, r'', markdown)
            # Replace \t with four spaces
            markdown = markdown.replace('\t', '    ')
            # Replace Related Articles heading with placeholder
            markdown = markdown.replace('## Связанные статьи', '--8<-- "related_topics_heading.md"')
            # Replace product name with placeholder
            markdown = markdown.replace('Comindware Platform', '{{ productName }}')
            # Reformat images with captions
            pattern = re.compile(r'(!\[(.*)\]\(.*\))\n\n\2', flags=re.MULTILINE)
            markdown = re.sub(pattern, r'_\1_', markdown)
            # Compile and add frontmatter
            frontmatter = '\n'.join([
                '---',
                f'title: {title}',
                f'kbId: {id}',
                '---',
                '\n'
                ])
            # Add link map to the bottom
            footer = '{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}\n'
            markdown = frontmatter + markdown + footer
            pattern = re.compile(r'`!\[.*\]\(.*\) *(.*?) *\{Article-ID:(\d+)\}.*?`', flags=re.MULTILINE)
            # markdown = re.sub(pattern, r'[\2](https://kb.comindware.ru/article.php?id=\3)', markdown)
            # markdown = re.sub(pattern, r'[\1](https://kb.comindware.ru/article.php?id=\2)', markdown)
            for result in re.finditer(pattern, markdown):
                articleId = result.group(2)
                c.execute(f"""
                    SELECT phpkb_articles.article_title 
                    FROM phpkb_articles
                    WHERE article_show='yes' 
                    AND phpkb_articles.article_id={articleId}
                    LIMIT 1
                    """)
                
                foundArticle = c.fetchall()
                if foundArticle:
                    articleName = foundArticle[0][0]
                    replacementRegex = fr'[{articleName}](https://kb.comindware.ru/article.php?id=\2)'
                    markdown = re.sub(pattern, replacementRegex, markdown, count=1)
            # Replace article links in markdown with URL from hyperlinks map
            pattern = r'\(https://kb\.comindware\.ru.+?((article\\?\.php\\?\?id=)|-)(\d+)(?(2)|\.html)(#?)(.*?)\)'
            foundLinks = re.finditer(pattern, markdown)
            for link in foundLinks:
                article_id = link.group(3)
                anchor = ''
                if link.group(4) == '#':
                    anchor = link.group(5)
                url = find_url_in_snippet(article_id, anchor)
                if url:
                    pattern = r'\(https://kb\.comindware\.ru.+?((article\\?\.php\\?\?id=)|-)({0})(?(2)|\.html).*?\)'.format(article_id)
                    markdown = re.sub(pattern, url, markdown, count=1)
                    print (f'Replaced {link.group(0)} with {url}')
            #markdown = markdown.replace('https://kb.comindware.ru/category.php?id=', '{{ kbCategoryURLPrefix }}')
            b.write(markdown)
            # print(html.escape(str(p)))
            pages += 1
    TOTAL_PAGES_IMPORTED += pages
    print("\nImported {} articles, total {}\n\n-----\n".format(pages, TOTAL_PAGES_IMPORTED))
    return pages


def fetchCategories(show='yes', status='private', language_id=2, parent_id=''):

    c = CONNECTION.cursor()    

    c.execute(f"""
            SELECT DISTINCT category_id, category_name, parent_id
            FROM phpkb_categories 
            WHERE category_show='{show}' 
            AND category_status = '{status}'
            AND phpkb_categories.language_id = {language_id}
            AND parent_id = '{parent_id}'
            """)
    categories = c.fetchall()
    return categories


def listCategories(categories):
    index = 1
    for id, title, parent_id in categories:
        print(f"{index}. {id}. {title}")
        index += 1

def main():
    
    global KB_ID_TO_TITLE_MAP
        
    KB_ID_TO_TITLE_MAP = loadMappingJson(KB_ID_TO_TITLE_MAP_FILE)
    
    if len(KB_ID_TO_TITLE_MAP) == 0:
        KB_ID_TO_TITLE_MAP = dict()
    
    with open(".serverCredentials.json", "r") as serverCredentialsFile: 
        
        serverCredentialsFileContent = serverCredentialsFile.read()
        serverCredentials = json.loads(serverCredentialsFileContent) if serverCredentialsFileContent else dict()
    
    sql_hostname = serverCredentials['sql_hostname'] or input("SQL_hostname:\n")
    ssh_host = serverCredentials['ssh_host'] or input("PHPKB host:\n")
    ssh_username = serverCredentials['ssh_username'] or input('SSH username:\n')
    ssh_password = getpass("SSH password:\n")
    sql_username = serverCredentials['sql_username'] or input("SQL username:\n")
    sql_password = getpass("SQL password:\n")
    sql_database = serverCredentials['sql_database'] or input("Database name:\n")
    sql_port = serverCredentials['sql_port'] or input("SQL remote port:\n")
    sql_port_local = serverCredentials['sql_port_local'] or input("SQL local port:\n")
    sql_ip = serverCredentials['sql_ip'] or input("SQL remote IP:\n")  
        
    # if input('Save credentials? Y / N').lower() == 'y':
    #     with open(".serverCredentials.json", "w") as serverCredentialsFile: 
    #         credentialsJson = json.dumps(serverCredentials, indent = 4)
    #         serverCredentialsFile.write(credentialsJson)

    server = SSHTunnelForwarder(
        ssh_host,
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=(sql_ip, sql_port),
        local_bind_address=(sql_ip, sql_port_local)
    )

    server.start()
    # print(server.local_bind_port)
    global CONNECTION
    # with server as tunnel:
    CONNECTION = mysql.connector.MySQLConnection(
        user = sql_username,
        password = sql_password,
        host = sql_ip,
        port = server.local_bind_port,
        database = sql_database
    )
    
    importChildren = ''
    categoryId = ''
    parent_category = ''
    categoryChoice = ''

    print('\nRoot categories:\n')

    while importChildren != 'y':
        
        
        categoryChoice = ''
        
        categories = fetchCategories(parent_id=categoryId)
        if parent_category: print("\nParent: {}. {}\n".format(categoryId, categoryTitle))
        if len(categories)>1: 
            parent_category = categories[0]
            listCategories(categories)
            print("\n---------\n")
            
            if importChildren.isnumeric() and int(importChildren) <= len(categories):
                    categoryChoice = int(importChildren)-1
                    importChildren = 'y'
            else:    
                while not (categoryChoice.isnumeric() and int(categoryChoice) <= len(categories)):
                    categoryChoice = input("Choose category to browse (1 to {}): ".format(len(categories)))
                    if categoryChoice.isnumeric() and int(categoryChoice) <= len(categories):
                        categoryChoice = int(categoryChoice)-1
                        break
                    else:
                        categoryChoice = ''
                        print ('Wrong category choice')
                
            
            categoryId = categories[categoryChoice][0]
            categoryTitle = categories[categoryChoice][1]  
            childrenCategories = fetchCategories(parent_id=categoryId)
            childrenCategoriesNumber = len(childrenCategories)
        
            print ("\nChosen category: {} {}".format(categoryId, categoryTitle))
            if childrenCategoriesNumber > 0:
                print ('\nIt has {} child categories:\n'.format(childrenCategoriesNumber))
                listCategories(childrenCategories)
                importChildren = input("\nEnter `Y` to import all child categories and articles. \n Or choose a category to browse (1 to {}). \n".format(childrenCategoriesNumber)).lower()
            else: 
                print ('\nIt has no child categories')
                importChildren = input("\nEnter `Y` to import all articles from this category. ".format(categoryId, categoryTitle)).lower()
                if importChildren !='y': 
                    print('Imported nothing')
                    break

    else:
        if categories[categoryChoice]:
            importCategoryChildren(categories[categoryChoice], KB_DIR)
        
    
    CONNECTION.close()
    server.close()
    server.stop()
    
def findFilenameByArticleId(article_id, docs_dir):
    """
    Find the filename in the specified docs directory containing the specified kbId.
    Uses a cached dictionary to speed up subsequent lookups.
    
    Args:
        article_id (str): The kbId to search for.
        docs_dir (str): The directory to scan for markdown files.
        
    Returns:
        str: The filename without the .md extension if found, else None.
    """
    global KB_ID_TO_FILENAME_MAP
    
    # Initialize and populate the mapping if not already done
    if KB_ID_TO_FILENAME_MAP is None:
        KB_ID_TO_FILENAME_MAP = {}
        if not os.path.isdir(docs_dir):
            raise FileNotFoundError(f"The directory '{docs_dir}' does not exist.")
        
        # Build the mapping from kbId to filenames
        for root, _, files in os.walk(docs_dir):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    filename = os.path.splitext(file)[0]
                    if not filename=='index':
                        with open(file_path, "r", encoding="utf-8") as f:
                            for line in f:
                                match = re.match(r"kbId:\s*(\S+)", line.strip())
                                if match:
                                    kb_id = match.group(1)
                                    KB_ID_TO_FILENAME_MAP[kb_id] = filename
                                    break  # Stop scanning this file after finding kbId
    
    foundFilename = KB_ID_TO_FILENAME_MAP.get(str(article_id))
    foundTitle = KB_ID_TO_TITLE_MAP.get(str(article_id))
    if not foundFilename:
            articleAnchor = find_url_in_snippet(article_id, None)
            if articleAnchor:
                articleAnchor = re.sub(r'\[(.*)\]', r'\1', articleAnchor)
                KB_ID_TO_FILENAME_MAP[str(article_id)] = articleAnchor
            elif foundTitle:
                KB_ID_TO_FILENAME_MAP[str(article_id)] = foundTitle
                
                
    # Lookup in the cached dictionary
    return KB_ID_TO_FILENAME_MAP.get(str(article_id))

def updateMappingJson(key, value, mapping, mappingFilename):
    mapping.update({str(key):value})
    with open(mappingFilename, "w") as mappingFile: 
        mappingJson = json.dumps(mapping, indent = 4, ensure_ascii=False)
        print(mappingJson)
        mappingFile.write(mappingJson)
        
def loadMappingJson(mappingFilename):

    with open(mappingFilename, "r") as mappingJsonFile: 
        mappingJsonFileContent = mappingJsonFile.read()
        mappingJson = json.loads(mappingJsonFileContent) if mappingJsonFileContent else dict()
        return mappingJson

if __name__ == "__main__":
    main()