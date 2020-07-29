import xml.etree.ElementTree as ET

data=ET.parse('Library.xml')
all=data.findall('dict/dict/dict')
i=0
for tree in all:
    for child in tree:
        if child.tag=='key' and child.text=='Name':
            print(child.text)
            i=i+1
print(i)
