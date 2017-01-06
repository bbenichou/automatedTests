from BasePage.Base_page_structure import *
from Pages.listingpage import *
from Pages.ProductPage import *

# Variables
iframeid = "fancybox-frame"
quickviewid = "product_addtocart_form"

# Assertions

# Locators

# Actions
def openquickview():
    gotolistingpage()
    driver.find_element_by_xpath(firstBoxPPimgXpath).click()

def assertquickviewopen():
    driver.switch_to_frame(driver.find_element_by_id(iframeid))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, quickviewid)))
    driver.switch_to_default_content()
