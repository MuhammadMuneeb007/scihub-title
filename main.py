import time
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.chrome.options import Options
import os
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.firefox.options import Options
import pymsgbox
import scrapers
from autologging import logged, traced
from csv import reader
from time import sleep
import requests
from bs4 import BeautifulSoup
import requests
import json
import shutil
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/save",  # Specify the directory to save the downloaded file
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "",  
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})


 


 
 
def getmearticle(title,direct):
    driver = webdriver.Chrome(options=chrome_options,executable_path=DRIVER_PATH)
    driver.get("https://sci-hub.se/")
    time.sleep(2)
    element = driver.find_element_by_xpath(".//*[@id='request']")    
    element.send_keys(title)
    try:
        time.sleep(2)
        element = driver.find_element_by_xpath(".//button[@type='submit']").click()    
        time.sleep(2)
        element = driver.find_element_by_xpath(".//*[@type='application/pdf']").get_attribute("src")  
        time.sleep(2)
        response = requests.get(element)

        if response.status_code == 200:
            local_pdf_path = direct

            # Save the PDF content to the local file
            with open(local_pdf_path, 'wb') as pdf_file:
                pdf_file.write(response.content)

            print(f"PDF downloaded and saved to {local_pdf_path}")
        else:
            print(f"Failed to download PDF. Status code: {response.status_code}")
    except:
        pass


# Set chrome driver path.
# Download the chromedriver link: https://chromedriver.chromium.org/downloads
# Place it in the directory.

DRIVER_PATH = 'chrome'+os.sep+'chromedriver'
title = "ImageNet Classification with Deep Convolutional Neural Networks"
directory = "./" # Current Directory
filename = "Article.pdf"
getmearticle(title,directory+os.sep+filename)    
 
        






















