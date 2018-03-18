import xml.etree.ElementTree as et
from pytz import timezone
import datetime
from xml.dom import minidom


text_from_input = input("write here url: ")
last_mod = datetime.datetime.now(timezone('Asia/Yerevan')).isoformat()
try:
    sitemap_file = open('sitemap.xml', 'r')
except IOError:
    open('sitemap.xml', 'w')
    sitemap_file = open('sitemap.xml', 'r')
first_url = False
if not '<?xml version="1.0" encoding="UTF-8"?>' in sitemap_file.read():
    first_url = True
sitemap_file.close()

def add_first_url(text_from_input, last_mod):
    root = et.Element('urlset')
    url = et.SubElement(root, 'url')
    loc = et.SubElement(url, 'loc')
    loc.text = 'http://freedom-dev.com/' + text_from_input
    lastmod = et.SubElement(url, 'lastmod')
    lastmod.text = last_mod
    tree = et.ElementTree(root)
    xmlstr = minidom.parseString(et.tostring(root)).toprettyxml(encoding="UTF-8")
    with open("sitemap.xml", "wb") as f:
        f.write(xmlstr)
    f.close()
    return ('url %s successfully added to sitemap' % text_from_input)

def update_sitemap(text_from_input, last_mod):
    tree = et.parse('sitemap.xml')
    root = tree.getroot()
    for childs in root:
        for child in childs:
            if child.tag == 'loc':
                ext = child.text.split('/')[-1]
                if text_from_input == ext:
                    return ('you yourself said that it must be unique :), url %s already exist, please write unique url' % text_from_input)
    new_url = et.SubElement(root, "url")
    loc = et.SubElement(new_url, 'loc')
    loc.text = 'http://freedom-dev.com/' + text_from_input
    lastmod = et.SubElement(new_url, 'lastmod')
    lastmod.text = last_mod
    xmlstr = minidom.parseString(et.tostring(root)).toprettyxml(indent="   ", encoding="UTF-8")
    with open("sitemap.xml", "wb") as f:
        f.write(xmlstr)
    f.close
    return ('url %s successfully added to sitemap' % text_from_input)

if first_url:
    result = add_first_url(text_from_input=text_from_input, last_mod=last_mod)
    print(result)
else:
    result = update_sitemap(text_from_input=text_from_input, last_mod=last_mod)
    print(result)

