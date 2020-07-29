import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import numpy as np



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location:')
data=urllib.request.urlopen(url,context=ctx).read()

print('Retrieved:',url)
print('Retrieved ',len(data), 'characters')
tree=ET.fromstring(data)
print('treelen',len(tree))

lst=tree.findall('comments/comment')
print('listlen',len(lst))
sum=0
num=[int(item.find('count').text) for item in lst]
for x in num:
    sum=sum+x
print(num)
print('count: ',len(lst))
print(sum)
