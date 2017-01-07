from BasePageStructure.Base_page_structure import *
from Pages.listingpage import *
from Pages.ProductPage import *
from Pages.QuickView import *

class confirmationpopup():
    # Variables
    iframeid = "fancybox-frame"
    confirmationmessageoneitem = "Your item has been added to your basket"
    confirmationmessagexpath = "//*[@id='added-products-details']/div[2]/h1"
    firstskunamexpath ="//*[@id='product_addtocart_form']/div[3]/div[3]/div[1]/div[1]/span[1]"
    firstskunameconfirmationmessagexpath ="//*[@id='added-products-details']/div[2]/ul/li/span"

    # Locators
    viewbasketbuttonXpath = "//*[@id='quickorder-checkout-link']/span"
    continueshoppingbuttonXpath = "//*[@id='quickorder-continue-link']/span"
    firstaddtobasketbuttonxpath ="//*[@id='product_addtocart_form']/div[3]/div[3]/div[1]/div[3]/button/span/span"

    def openconfirmationpopuponeitem():
        openquickview()
        driver.switch_to_frame(driver.find_element_by_id(iframeid))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, addtobasketbuttonsClass)))
        skuname = driver.find_element_by_xpath(firstskunamexpath).text
        driver.find_element_by_xpath(firstaddtobasketbuttonxpath).click()

    def closeconfirmationpopup():
        driver.switch_to_frame(driver.find_element_by_id(iframeid))
        driver.find_element_by_xpath(continueshoppingbuttonXpath).click()
        driver.switch_to_default_content()
        WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.ID,iframeid)))

    def assertconfirmoneitem():
        skuname = openconfirmationpopuponeitem()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,confirmationmessagexpath)))
        assert skuname in driver.find_element_by_xpath(firstskunameconfirmationmessagexpath).text
        driver.switch_to_default_content()
