import urllib.request,urllib.parse,urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url=input('Enter Location :')
data=urllib.request.urlopen(url,context=ctx).read().decode()

print('Retrieving:',url)
print('Retrieved:',len(data), 'characters')


s=0
js=json.loads(data)
for item in js['comments']:
    s=s+int(item['count'])
print('Count:',len(js['comments']))
print('Sum:',s)
