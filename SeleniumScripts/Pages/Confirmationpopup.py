from BasePage.Base_page_structure import *

# Variables

# Locators
viewbasketbuttonXpath = "//*[@id='quickorder-checkout-link']/span"
continueshoppingbuttonXpath = "//*[@id='quickorder-continue-link']/span"


def confpopupclickcontinueshopping():
    driver.switch_to_frame(driver.find_element_by_id("fancybox-frame"))
    driver.find_element_by_xpath(continueshoppingbuttonXpath).click()