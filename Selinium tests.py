from tqdm import tqdm
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
if __name__ == '__main__':
	user_name = "Conn205@gmail.com"
	password = "Panthers"
	driver = webdriver.Firefox()
	driver.get("https://www.facebook.com")
	element = driver.find_element_by_id("email")
	element.send_keys(user_name)
	element = driver.find_element_by_id("pass")
	element.send_keys(password)
	element.send_keys(Keys.RETURN)
	element.close()