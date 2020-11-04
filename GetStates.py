from urllib.request import urlopen
from tqdm import tqdm
from bs4 import BeautifulSoup
import sys

__author__ = "Connor Nelson"

# Opening and Reading in HTML File
html = urlopen(
    "https://abbreviations.yourdictionary.com/articles/state-abbrev.html")
bsObj = BeautifulSoup(html, "html.parser")
# Get the list objects
linkedList = bsObj.findAll('li')
for i in range(len(linkedList)):
    linkedList[i] = linkedList[i].text
# print(linkedList)
indexAL = linkedList.index("Alabama - AL")
# print(indexAL)
indexWY = linkedList.index("Wyoming - WY")
linkedList = linkedList[indexAL:indexWY]
print(linkedList)
# Take first 50 and put them in a list
# for i in tqdm(range(100)):
# 	goodList.append(linkedList[i].text)
# Print List
#print(goodList)

# Testing Terminal
