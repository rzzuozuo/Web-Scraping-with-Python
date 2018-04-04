from urllib.request import urlopen
from bs4 import BeautifulSoup
import re #正则表达式库
import random #随机数
import datetime

def openUrl(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        raise

    return html

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

random.seed(datetime.datetime.now()) #使用当前时间提供随机数种子

def getLinks(articleUrl):
    bsObj = bsOpenUrl("https://en.wikipedia.org" + articleUrl)
    if bsObj == None:
        print("URL could not open")
    else:
        return bsObj.find("div",{"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$")) # 在id=bodyContent 的div里查找满足 "/wiki/"开头 ，不含“：” 的 a

links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links) -1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
