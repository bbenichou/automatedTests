from BasePage.Base_page_structure import *


# Variables

# Assertions
megamenufirstlinkXpath = "//*[@id='custommenu-nav']/li[1]/a[1]"

# Locators

# Actions
def gotolistingpage():
    getdomain()
    url = getdomain()
    driver.get(url)
    driver.maximize_window()
    impwait()
    driver.find_element_by_xpath(megamenufirstlinkXpath).click()
    impwait()