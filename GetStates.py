from urllib.request import urlopen 
from bs4 import BeautifulSoup
import sys
import re

__author__ = "Connor Nelson"

#Opening and Reading in HTML
html = urlopen("https://abbreviations.yourdictionary.com/articles/state-abbrev.html")
bsObj = BeautifulSoup(html, "html.parser")
linkedList = bsObj.findAll('li')
goodList = []
for item in linkedList:
	goodList.append(item.text)
print(goodList[:50])

