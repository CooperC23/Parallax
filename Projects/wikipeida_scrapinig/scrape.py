import requests
from bs4 import BeautifulSoup
from PageTitle import getPageTitle  
import urllib3
import re
import unicodedata

toggle = False
possibleLinks = []
linkCounter = 0
nextLink = ""
url = 'https://en.wikipedia.org/wiki/Truth'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))
    #urls.append(link)

html = str(soup)
result = html.find('<b>Truth')
print(result)
print(getPageTitle(url))
for link in urls:
    
    newLink = str(link)
    if newLink != 'None':
        
        print(type(link))
        index = html.find(newLink)
 #   if index > result:
#        if index !=45555: 
            #possibleLinks.append(urls.index(link))
