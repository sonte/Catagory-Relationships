from xml.dom import minidom
import xml.etree.ElementTree as et

__author__ = 'sonte'
relationDictionary = dict()
doc = et.parse('category_relationships.xml')
child = doc.findall('category_relationship')
x = 0

while (x < len(child)):
    if int(child[x][0].text) in relationDictionary.keys():
        relationDictionary[int(child[x][0].text)].append(int(child[x][1].text))
    else:
        relationDictionary[int(child[x][0].text)] = [int(child[x][1].text)]
    x = x + 1
print(relationDictionary)