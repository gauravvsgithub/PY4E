import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
url = input('Enter url : ')
count1 = input('enter count : ')
counts = int(count1)
pos = input('enter position : ')
for count in range(0,counts):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    url = tags[int (pos)-1].get('href',None)

#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html,'html.parser')
#tags = soup('a')
print(url.contents[0])
#print(url)
