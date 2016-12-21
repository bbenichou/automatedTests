from selenium import webdriver
from selenium.webdriver import ActionChains
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
