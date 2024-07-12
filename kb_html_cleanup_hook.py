import bs4
import html
import re
import json

def on_post_page (output, **kwargs):
    kb_html = output.replace('class="admonition note"', 'class="notice notice-info"')
    kb_html = kb_html.replace('class="admonition warning"', 'class="notice notice-warning"')
    kb_html = kb_html.replace('class="admonition question"', 'class="notice notice-success"')
    
    p = bs4.BeautifulSoup(kb_html, 'html.parser')
    h1 = p.find('h1')
    if (h1):
        print ('deleting redundant H1: ' + h1.string)
        h1.decompose()
    for i in p.find_all('i', class_=re.compile("fa.+")):
        i.string = '&zwnj;' + '<!--icon-->'
    # for i in p.find_all('p', class_='admonition-title'):
    #        print ('making admonition title bold:' + i.string)
    #        i.string = '<strong>' + str(i.string) + '</strong>'
            
    for i in p.find_all('a'):
        #with open("links_mapping.txt", "a+") as file:
            # json.loads(file.read())
            #print('Found link: ' + str(i.string) + 'href=' + str(i['href']))
            #json_entry = json.dumps({str(i.string): i['href']})
            # kb_link =  input('Enter KB article link:')
            #if kb_link:
            #    i['href']=kb_link
            #    file.write('')
        if i.get('class'):
            i['class'].append("mkdocs_imported_link")
        else: 
            i['class'] = "mkdocs_imported_link"
    # p = p.body
    return html.unescape(str(p))