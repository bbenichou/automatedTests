from Pages.QuickViewPage import *


class ConfirmationPopUp(QuickView):
    # Variables
    iframeid = "fancybox-frame"
    confirmationmessageoneitem = "Your item has been added to your basket"
    confirmationmessagexpath = "//*[@id='added-products-details']/div[2]/h1"
    firstskunamexpath ="//*[@id='product_addtocart_form']/div[3]/div[3]/div[1]/div[1]/span[1]"
    firstskunameconfirmationmessagexpath ="//*[@id='added-products-details']/div[2]/ul/li/span"
    addtobasketbuttonsClass = "btn-cart"
    skuname = ''

    # Locators
    viewbasketbuttonXpath = "//*[@id='quickorder-checkout-link']/span"
    continueshoppingbuttonXpath = "//*[@id='quickorder-continue-link']/span"
    firstaddtobasketbuttonxpath ="//*[@id='product_addtocart_form']/div[3]/div[3]/div[1]/div[3]/button/span/span"

    def openconfirmationpopuponeitem(self):
        QuickView.openquickview(self)
        self.driver.switch_to_frame(self.driver.find_element_by_id(self.iframeid))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, self.addtobasketbuttonsClass)))
        skuname = self.driver.find_element_by_xpath(self.firstskunamexpath).text
        self.driver.find_element_by_xpath(self.firstaddtobasketbuttonxpath).click()
        return skuname

    def closeconfirmationpopup(self):
        self.driver.switch_to_frame(self.driver.find_element_by_id(self.iframeid))
        self.driver.find_element_by_xpath(self.continueshoppingbuttonXpath).click()
        self.driver.switch_to_default_content()
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located((By.ID,self.iframeid)))

    def assertconfirmoneitem(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.confirmationmessagexpath)))
        assert self.skuname in self.driver.find_element_by_xpath(self.firstskunameconfirmationmessagexpath).text
        self.driver.switch_to_default_content()
