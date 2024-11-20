import mysql.connector
# import sshtunnel
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

TOTAL_PAGES_UPDATED = 0
CONNECTION = None
# sshtunnel.SSH_TIMEOUT=0.5
# sshtunnel.TUNNEL_TIMEOUT=20.0
MAPPING = dict()


def updateCategoryChildren(parent):
    c = CONNECTION.cursor(buffered=True)
    
    id = parent[0]
    title = parent[1]
    parentId = parent[2]
  
    c.execute(f"""
        SELECT DISTINCT (category_id), category_name, parent_id
        FROM phpkb_categories 
        WHERE 
        -- category_show='yes' 
        -- AND 
        category_status = 'public'
        AND phpkb_categories.language_id = 2
        AND parent_id = {id}
        """)
    children = c.fetchall()
    print(f"\n-----\n\nCategory {id}. {title}. Children: {children}\n")
    print(f'Updating articles from Category {id}. {title}.')
    updateArticlesInCategory(id)
    for child in children:
        updateCategoryChildren(child)
    return children
    
        
def updateArticlesInCategory (category_id):
    c = CONNECTION.cursor(buffered=True)
    c.execute(f"""
            SELECT DISTINCT (phpkb_articles.article_id), phpkb_articles.article_content, phpkb_articles.article_title 
            FROM phpkb_articles, phpkb_relations, phpkb_categories 
            WHERE 
            -- article_show='yes' 
            -- AND 
            phpkb_relations.category_id = {category_id} 
            AND phpkb_relations.article_id = phpkb_articles.article_id
            """)
    
    articles = c.fetchall()
    global TOTAL_PAGES_UPDATED
    pages = 0
    for id, content, title in articles:
        sanitizedTitle=sanitize_filename(title)
        filename = f"{id} - {sanitizedTitle}"
        print ('    Updating article: ' + filename)
        pages += 1
        updateArticleLinks(id)
    TOTAL_PAGES_UPDATED += pages
    print(f"\nUpdated {pages} articles, total {TOTAL_PAGES_UPDATED}\n\n-----\n")
    return pages


def updateArticleLinks(article_id):
    
    c = CONNECTION.cursor() #(buffered=True)
    c.execute(f"""
            SELECT article_content from phpkb_articles WHERE article_id={article_id};
            """)
    
    article_content = html.unescape(str(c.fetchone()[0]))
      
    for oldArticleId in MAPPING['Articles'].keys():
    
        newArticleId = MAPPING['Articles'][oldArticleId]
        
        pattern = re.compile(fr'data-value="{oldArticleId}"', flags=re.MULTILINE)
        replacementRegex = fr'data-value="{newArticleId}"'
        if len(re.findall(pattern, article_content))>0:
            article_content = re.sub(pattern, replacementRegex, article_content)
            print(f'Replaced article markers {oldArticleId} : {newArticleId}')


        pattern = re.compile(fr'Article-ID:{oldArticleId}', flags=re.MULTILINE)
        replacementRegex = fr'Article-ID:{newArticleId}'
        if len(re.findall(pattern, article_content))>0:
            article_content = re.sub(pattern, replacementRegex, article_content)
            print(f'Replaced article markers {oldArticleId} : {newArticleId}')

        pattern = re.compile(fr'article\.php\?id={oldArticleId}', flags=re.MULTILINE)
        replacementRegex = fr'article\.php\?id={newArticleId}'
        if len(re.findall(pattern, article_content))>0:
            article_content = re.sub(pattern, replacementRegex, article_content)
            print(f'Replaced article links {oldArticleId} : {newArticleId}')
        
    for oldCategoryId in MAPPING['Categories'].keys():
    
        newCategoryId = MAPPING['Categories'][oldCategoryId]

        pattern = re.compile(fr'category\.php\?id={oldCategoryId}', flags=re.MULTILINE)
        replacementRegex = fr'category\.php\?id={newCategoryId}'
        if len(re.findall(pattern, article_content))>0:
            article_content = re.sub(pattern, replacementRegex, article_content)
            print(f'Replaced category links {oldCategoryId} : {newCategoryId}')
    
    pattern = re.compile(fr'Comindware Business Application Platform', flags=re.MULTILINE)
    replacementRegex = fr'Comindware Platform'
    if len(re.findall(pattern, article_content))>0:
        article_content = re.sub(pattern, replacementRegex, article_content)
        print(f'Replaced product name with Comindware Platform')
        
    pattern = re.compile(fr'(Comindware )?Architect', flags=re.MULTILINE)
    replacementRegex = fr'«Архитектор»'
    if len(re.findall(pattern, article_content))>0:
        article_content = re.sub(pattern, replacementRegex, article_content)
        print(f'Replaced Comindware Architect with «Архитектор»')
    
    # # print(f'Updating links in article {article_id}')
    
    article_content = html.escape(article_content)

   
    try:
        print("execution", len(article_content))
        c.execute("""
                UPDATE phpkb_articles 
                SET article_content=%s 
                WHERE article_id=%s;
                """, (article_content, article_id))
    except:
        print("Couldn't update the article")
        exit()
    
def fetchCategories(show='yes', status='public', language_id=2, parent_id=''):

    c = CONNECTION.cursor()    

    c.execute(f"""
            SELECT DISTINCT category_id, category_name, parent_id
            FROM phpkb_categories 
            WHERE 
            -- category_show = '{show}' 
            -- AND 
            category_status = '{status}'
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
    
    global MAPPING
    
    MAPPING = loadMappingJson()
    
    if len(MAPPING) == 0:
        print('Empty .mapping.json')
        exit()
    
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
    
    updateChildren = ''
    categoryId = '298'
    parent_category = ''
    categoryChoice = ''

    print('\nRoot categories:\n')

    while updateChildren != 'y':
        
        
        categoryChoice = ''
        categories = fetchCategories(parent_id=categoryId)
        if parent_category: print("\nParent: {}. {}\n".format(categoryId, categoryTitle))
        if len(categories)>1: 
            parent_category = categories[0]
            listCategories(categories)
            print("\n---------\n")
            
            if updateChildren.isnumeric() and int(updateChildren) <= len(categories):
                    categoryChoice = int(updateChildren)-1
                    updateChildren = 'y'
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
                updateChildren = input("\nEnter `Y` to update the category and all its child categories and articles. \n Or choose a category to browse (1 to {}). \n".format(childrenCategoriesNumber)).lower()
            else: 
                print ('\nIt has no child categories')
                updateChildren = input("\nEnter `Y` to update the category and all articles from this category. ".format(categoryId, categoryTitle)).lower()
                if updateChildren !='y': 
                    print('Updated nothing')
                    break

    else:
        if categories[categoryChoice]:
            updateCategoryChildren(categories[categoryChoice])
        
    
    CONNECTION.close()
    server.close()
    server.stop()
       
def loadMappingJson():

    with open(".mapping.json", "r") as mappingJsonFile: 
        mappingJsonFileContent = mappingJsonFile.read()
        mappingJson = json.loads(mappingJsonFileContent) if mappingJsonFileContent else dict()
        return mappingJson

if __name__ == "__main__":
    main()