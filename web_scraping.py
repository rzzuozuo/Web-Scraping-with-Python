from urllib.request import urlopen
from bs4 import BeautifulSoup
import re #正则表达式库

def openUrl(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None

def bsOpenUrl(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
    except AttributeError as e:
        return None
    return bsObj
bsObj = bsOpenUrl("https://en.wikipedia.org/wiki/Kevin_Bacon")
if bsObj == None:
    print("url could not open")

for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$")): # 在id=bodyContent 的div里查找满足 "/wiki/"开头 ，不含“：” 的 a
        if 'href' in link.attrs:
            print(link.attrs['href'])
