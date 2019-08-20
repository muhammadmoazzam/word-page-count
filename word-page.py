import os, zipfile, xml.dom.minidom, sys, getopt

if len(sys.argv) != 2:
    print("Usage: word-page.py <filename>\nRe-Run with given usage instruction")
    sys.exit(1)
document = zipfile.ZipFile(sys.argv[1])
dxml = document.read('docProps/app.xml')
uglyXml = xml.dom.minidom.parseString(dxml)
page = uglyXml.getElementsByTagName('Pages')[0].childNodes[0].nodeValue
print("Word Page count: " + page)
