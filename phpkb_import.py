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

class myparser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			print("IMG tag with attrs %s\n" % repr(attrs))

import os.path

import json

from sshtunnel import SSHTunnelForwarder

THIS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))
importPath = input('Path to import: ') 
KB_DIR = os.path.dirname(importPath) if importPath else 'phpkb_import'
TOTAL_PAGES_IMPORTED = 0
CONNECTION = ''

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

def importCategoryChildren(parent, categoryDirectory):
        # category = dict()
        # category['id', 'title', 'parent_id'] = parent
        # print(category)
        id = parent[0]
        title = parent[1]
        # print(id, title)
        
        #for id, title, parent_id, in parent:
        c4 = CONNECTION.cursor()    
        c4.execute("""
            SELECT DISTINCT (category_id), category_name, parent_id
            FROM phpkb_categories 
            WHERE category_show='yes' 
            AND category_status = 'public'
            AND phpkb_categories.language_id = 2
            AND parent_id = {}
            """.format(id))
        children = c4.fetchall()
        print("\n-----\n\nCategory {}. {}. Children: {}\n".format(id, title, children))
        dirName = sanitize_filename('{}. {}'.format(id, title))
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
    #c2 = CONNECTION.cursor()
    c.execute("""
            SELECT DISTINCT (phpkb_articles.article_id), phpkb_articles.article_content, phpkb_articles.article_title 
            FROM phpkb_articles, phpkb_relations, phpkb_categories 
            WHERE article_show='yes' 
            AND phpkb_relations.category_id = {categoryId} 
            AND phpkb_relations.article_id = phpkb_articles.article_id
            """.format(categoryId = categoryId))
    
    articles = c.fetchall()
    global TOTAL_PAGES_IMPORTED
    pages = 0
    for id, content, title in articles:
     
        # if os.path.exists(os.path.join(categoryDir, "article-{id}-{title}.md".format( id=id, title= sanitize_filename(title))): continue
        filename = os.path.join(categoryDir, "article-{id}-{title}.md".format( id=id, title= sanitize_filename(title)))
        print ('    Importing article: ' + filename)
        
        with open(filename, "w+") as b:
            
            p = bs4.BeautifulSoup(html.unescape(content), 'html.parser')
            article_title = p.new_tag("h1")
            article_title.string=title
            p.insert(0, article_title)
            # b.write(html.escape(str(p)))                
            # b.write(str(p))
            markdown = MarkdownConverter(heading_style='ATX', bullets='-', escape_misc=False).convert_soup(p)
            pattern = re.compile(r'^\n^\n\n*', flags=re.MULTILINE)
            markdown = re.sub(pattern, r'\n', markdown)
            # Remove redundant TOC
            pattern = re.compile(r'## Содержание.*\n*(.*\t*-.*\n)*\n', flags=re.MULTILINE)
            markdown = re.sub(pattern, r'', markdown)
            # Remove redundant [*‌* К началу](#) links
            pattern = re.compile(r'\[.*К началу\]\(#\)', flags=re.MULTILINE)
            markdown = re.sub(pattern, r'', markdown)
            # Compile and add frontmatter
            frontmatter = '\n'.join([
                '---',
                'title: {}',
                'kbId: {}',
                '---',
                '\n'
                ]).format(title, id)
            markdown = frontmatter + markdown
            pattern = re.compile(r'`!\[.*\]\(.*\) *(.*?) *\{Article-ID:(\d+)\}.*?`', flags=re.MULTILINE)
            # markdown = re.sub(pattern, r'[\2](https://kb.comindware.ru/article.php?id=\3)', markdown)
            # markdown = re.sub(pattern, r'[\1](https://kb.comindware.ru/article.php?id=\2)', markdown)
            for result in re.finditer(pattern, markdown):
                articleId = result.group(2)
                c.execute("""
                    SELECT phpkb_articles.article_title 
                    FROM phpkb_articles
                    WHERE article_show='yes' 
                    AND phpkb_articles.article_id={article_id}
                    LIMIT 1
                    """.format(article_id = articleId))
                
                foundArticle = c.fetchall()
                if foundArticle:
                    articleName = foundArticle[0][0]
                    replacementRegex = r'[{0}](https://kb.comindware.ru/article.php?id=\2)'.format(articleName)
                    markdown = re.sub(pattern, replacementRegex, markdown, count=1)
            b.write(markdown)
            # print(html.escape(str(p)))
            pages += 1
    TOTAL_PAGES_IMPORTED += pages
    print("\nImported {} articles, total {}\n\n-----\n".format(pages, TOTAL_PAGES_IMPORTED))
    return pages


def fetchCategories(show='yes', status='public', language_id=2, parent_id=''):

    c = CONNECTION.cursor()    

    c.execute("""
            SELECT DISTINCT category_id, category_name, parent_id
            FROM phpkb_categories 
            WHERE category_show='yes' 
            AND category_status = 'public'
            AND phpkb_categories.language_id = 2
            AND parent_id = '{parent_id}'
            """.format(parent_id = parent_id))

    categories = c.fetchall()
    return categories


def listCategories(categories):
    index = 1
    for id, title, parent_id in categories:
        print("{}. {}. {}".format(index, id, title))
        index += 1

def main():
    
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

if __name__ == "__main__":
    main()