import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup

url1 = input('Enter : ')
html1 = urllib.request.urlopen(url1).read()
soup = BeautifulSoup(html1,'html.parser')
tags = soup ('span')

print(tags)
#total=0
#for tag in tags:
#    total = total+ int(tag.contents[0])
#print(total)
