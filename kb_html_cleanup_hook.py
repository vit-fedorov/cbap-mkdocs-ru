import bs4
import html
import re
import json
import pathlib


def on_post_page (output, **kwargs):
    kb_html = output.replace('class="admonition note"', 'class="notice notice-info"')
    kb_html = kb_html.replace('class="admonition warning"', 'class="notice notice-warning"')
    kb_html = kb_html.replace('class="admonition question"', 'class="notice notice-success"')
    
    
    
    p = bs4.BeautifulSoup(kb_html, 'html.parser')
    
    # Delete H1 tags, they are redundant for PHPKB
    h1 = p.find('h1')
    if (h1):
        # print ('deleting redundant H1: ' + h1.string)
        h1.decompose()
    
    # Add &zwnj; within Fontawesome icons, otherwise PHPKB will delete them
    for i in p.find_all('i', class_=re.compile("fa.+")):
        i.string = '&zwnj;' + '<!--icon-->'
    
    # Add class="colored_numbers_list" to all ordered lists lists
        for i in p.find_all('ol'):
            i['class'] = 'colored_numbers_list'
            
    # Add style="width: 100%;" to all <tables>
    for i in p.find_all('table'):
        i['style'] = 'width: 100%;'
        
    # Add class="screenshot_with_caption" to figures
    for i in p.find_all('figure'):
        i['class'] = 'screenshot_with_caption'
        i.find('figcaption')['class'] = 'caption'
        
    # Base all image links on https://kb.comindware.ru/assets/
    for i in p.find_all('img'):
        filename = pathlib.PurePath(str(i['src'])).name
        i['src'] = 'https://kb.comindware.ru/assets/' + filename

    # Classify all links as imported from MkDocs            
    for i in p.find_all('a'):
        if i.get('class'):
            i['class'].append("mkdocs_imported_link")
        else: 
            i['class'] = "mkdocs_imported_link"
    
    #  Fix code blocks for PHPKB
    for i in p.find_all('pre'):
        pattern = re.compile(r'(\s*<span.*)\n', flags=re.MULTILINE)
        pre = str(i)
        pre = re.sub(pattern, 
                      r'<code>\1</code><br/>\n', 
                      pre)
        i.replace_with(bs4.BeautifulSoup(pre, 'html.parser'))
        
    p = p.body # do not use prettify(), it adds redundant spaces in PHPKB
    
    return html.unescape(str(p))