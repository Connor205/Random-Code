from urllib.request import urlopen
from tqdm import tqdm
from bs4 import BeautifulSoup
import sys

__author__ = "Connor Nelson"

# Opening and Reading in HTML File
html = urlopen("https://abbreviations.yourdictionary.com/articles/state-abbrev.html")
bsObj = BeautifulSoup(html, "html.parser")
# Get the list objects
linkedList = bsObj.findAll('li')
goodList = []
# Take first 50 and put them in a list
for i in tqdm(range(50)):
	goodList.append(linkedList[i].text)
 # Print List
print(goodList)

# Testing Terminal
