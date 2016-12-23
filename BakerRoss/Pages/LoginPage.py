from BasePage.Base_page_structure import *

# Variables
email = getloginvalue()
password = getpassvalue()
path = ("/customer/account/login/")

# Assertions
nameAssert = "Ben"

# Locators
emailXpath = "//*[@id='email']"
passXpath = "//*[@id='pass']"
loginButtonXpath = "//*[@id='send2']/span/span"
welcomeTextXpath = "//*[@id='page']/div[4]/div/div[3]/div[2]/div/div[2]/h2"
logoutLinkXpath = "//*[@id='page']/div[1]/div/ul[2]/li[2]/a"
headerUsernameXpath = "//*[@id='page']/div[1]/div/ul[1]/li[1]"

# Actions
def inputemail():
    driver.find_element_by_xpath(emailXpath).send_keys(email)

def inputpass():
    driver.find_element_by_xpath(passXpath).send_keys(password)

def clicklogin():
    driver.find_element_by_xpath(loginButtonXpath).click()

def logout():
    driver.find_element_by_xpath(logoutLinkXpath).click()

def assertloggedin():
    assert nameAssert in driver.find_element_by_xpath(headerUsernameXpath).text
    assert nameAssert in driver.find_element_by_xpath(welcomeTextXpath).text

def assertloggedout():
    assert nameAssert not in driver.find_element_by_xpath(headerUsernameXpath).text
