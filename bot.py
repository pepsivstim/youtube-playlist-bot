from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/playlist?list=PLcysmcZSZqKQ5FAiCQlO_kOoSSNcsjBgK")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

content = driver.page_source
#print(content)
soup = BeautifulSoup(content, features="html.parser")
#print(soup.prettify())

found = "index"
i = 0
for link in soup.find_all('a'):

    i = i + 1
    if found in link:
        print(link.get('href'))
        print(i)
