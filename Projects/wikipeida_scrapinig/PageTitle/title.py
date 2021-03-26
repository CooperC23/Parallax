from bs4 import BeautifulSoup
import requests

def getPageTitle(URL):
    url = URL
    pageTitle = ""
    temp = ""
    toggle = True
    
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for title in soup.find_all('title'):
        pageTitle = title.get_text()

    while toggle != False:
        for Character in pageTitle:
            if Character == "-":
                toggle = False
            if toggle == True:
                temp += Character
    pageTitle = temp
    return pageTitle
