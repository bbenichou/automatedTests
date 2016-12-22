from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging

# Variables
driver = webdriver.Chrome("C:\\seleniumDriver\\chromedriver_win32\\chromedriver.exe")

# Locators

# Actions

def impwait():
    driver.implicitly_wait(5)

def gotourl(url):
    driver.get(url)
    driver.maximize_window()

def log():
    logging.basicConfig(filename='L:\\Work\\testlogfile.cslog', level=logging.DEBUG)
