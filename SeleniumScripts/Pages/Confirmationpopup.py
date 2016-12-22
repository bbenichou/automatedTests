from BasePage.Base_page_structure import *

# Variables
iframeid = "fancybox-frame"

# Locators
viewbasketbuttonXpath = "//*[@id='quickorder-checkout-link']/span"
continueshoppingbuttonXpath = "//*[@id='quickorder-continue-link']/span"

def confpopupclickcontinueshopping():
    driver.switch_to_frame(driver.find_element_by_id(iframeid))
    driver.find_element_by_xpath(continueshoppingbuttonXpath).click()
    driver.switch_to_default_content()
    WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.ID,iframeid)))
