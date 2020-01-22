from tqdm import tqdm
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
	followersPage = requests.get("https://www.instagram.com/connel205/followers/?hl=en")
	followersPage_BS = BeautifulSoup(followersPage.text, "html.parser")
	print(followersPage_BS)
	followersList = followersPage_BS.findAll('a', {"class" : "FPmhX notranslate  _0imsa "})
	print(followersList)