from selenium import webdriver

driver = webdriver.Chrome("C:\\seleniumDriver\\chromedriver_win32\\chromedriver.exe")
timeout = 30

def impwait():
    driver.implicitly_wait(5)

def gotourl(url):
    driver.get(url)
    driver.maximize_window()