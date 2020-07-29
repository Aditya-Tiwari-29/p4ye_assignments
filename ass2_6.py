import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://py4e-data.dr-chuck.net/json?'
local=input('Enter Location:')
url = serviceurl + urllib.parse.urlencode({'address':local,'key':42})
print('Retrieving:',url)
data=urllib.request.urlopen(url).read().decode()
print('Retrieved:',len(data),'characters')
js=json.loads(data)
print(json.dumps(js,indent=4))
print('Place id',js['results'][0]['place_id'])
