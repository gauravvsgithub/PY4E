import urllib.request ,urllib.parse, urllib.error
import json
apikey=False
if apikey is False:
    apikey=42
    serviceurl='https://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

address=input('Enter Location : ')
dctnry=dict()
dctnry['address'] = address
if apikey is not False:
    dctnry['key']=apikey

url=serviceurl+urllib.parse.urlencode(dctnry)
urlhandle=urllib.request.urlopen(url)
data=urlhandle.read().decode()
try:
    js = json.loads(data)
except:
    js = None
#print(js["results"][0]["place_id"])
    #print(item)
    #print('\n')


print(js)
#print(data)
