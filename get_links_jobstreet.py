from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import pickle
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np


drv_path = "C:\\Users\\LENOVO\\Documents\\chromedriver\\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(drv_path, options=chrome_options)
# driver.minimize_window()

links = []
for i in range(501,551):
	url = 'https://www.jobstreet.co.id/id/job-search/job-vacancy.php?pg='+str(i)
	driver.get(url)
	print("--------------------------------")
	print('Page '+str(i))
	print("--------------------------------")
	elems = driver.find_elements_by_xpath("//h1[@class='FYwKg _1GAuD C6ZIU_1 _6ufcS_1 _27Shq_1 sQuda_1']")
	for elem in elems:
		# print(elem.text)
		link = elem.find_element_by_css_selector('a').get_attribute('href')
		links.append(link)
		# print(link)
	time.sleep(5)

import csv

with open("file8.txt", "w") as output:
    output.write(str(links))