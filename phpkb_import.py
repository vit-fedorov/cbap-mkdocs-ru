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

class myparser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			print("IMG tag with attrs %s\n" % repr(attrs))

import os.path

from sshtunnel import SSHTunnelForwarder

THIS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))
KB_DIR = os.path.join(THIS_FILE_DIR, 'phpkb_import')
TOTAL_PAGES_IMPORTED = 0
CONNECTION = ''

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
        if os.path.exists(os.path.join(categoryDir, "article-{id}-{title}.md".format( id=id, title= sanitize_filename(title)))): 
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
    # c2 = CONNECTION.cursor()
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
            frontmatter = '\n'.join([
                '---',
                'title: {}',
                'kbId: {}',
                '---',
                ''
                ]).format(title, id)
            markdown = frontmatter + markdown
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
    
    # sql_hostname = 'localhost'
    ssh_host = input("PHPKB host:\n")
    ssh_username = input('Username:\n')
    ssh_password = getpass("Password:\n")
    # ssh_port = 22
    sql_username = ssh_username
    sql_password = ssh_password
    sql_database = 'phpkbv9'
    sql_port = 3306
    sql_port_local = 3307
    sql_ip = '127.0.0.1'

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

            while not (categoryChoice.isnumeric() and int(categoryChoice) <= len(categories)):
                categoryChoice = input("Choose category to import (1 to {}): ".format(len(categories)))
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
                importChildren = input("\nImport all child categories and articles? Y/N: ".format(categoryId, categoryTitle)).lower() 
            else: 
                print ('\nIt has no child categories')
                importChildren = input("\nImport all articles from this category? Y/N: ".format(categoryId, categoryTitle)).lower()
                if importChildren !='y': 
                    print('Imported nothing')
                    break

    else:
        if categories[categoryChoice]:
            importCategoryChildren(categories[categoryChoice], KB_DIR)
        
    
    server.stop()

if __name__ == "__main__":
    main()