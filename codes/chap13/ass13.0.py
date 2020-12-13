import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL : ')

handle = urllib.request.urlopen(url)
data = handle.read()
tree = ET.fromstring(data.decode())
lst = tree.findall('.//count')
total=0
for itm in lst:
    total = total + int(itm.text)
print(total)
