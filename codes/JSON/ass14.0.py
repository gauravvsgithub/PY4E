import urllib.request , urllib.parse, urllib.error
import json
address = input('location ')
urlhandle=urllib.request.urlopen(address)
data=urlhandle.read().decode()
info = json.loads(data)
total=0
for item in info["comments"]:
    total=total+int(item["count"])
print(total)
