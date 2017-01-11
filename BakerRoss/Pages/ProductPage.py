from BasePageStructure.Base_page_structure import *
from Pages.ConfirmationpopuPage import ConfirmationPopUp
from selenium.webdriver import ActionChains

class ProductPage(BasePage):

    # Variables
    listingPagePath = ("/arts-and-crafts")
    iframeid = "fancybox-frame"

    # Locators
    addtobasketbuttonsClass = "btn-cart"
    itemstopcartXpath = "//*[@id='cartHeader']/span"
    continueshoppingbuttonXpath = "//*[@id='quickorder-continue-link']/span"

    # Assertions

    # Action
    def addtobasket(self):
        addbuttons = self.driver.find_elements_by_class_name(self.addtobasketbuttonsClass)
        addbuttons_len = len(addbuttons)
        for i in range(0,addbuttons_len):
            self.driver.find_elements_by_class_name(self.addtobasketbuttonsClass).__getitem__(i).click()
            ConfirmationPopUp.closeconfirmationpopup(self)
            self.driver.switch_to_default_content()

    def assertaddtobasket(self):
        addbuttons = self.driver.find_elements_by_class_name(self.addtobasketbuttonsClass)
        addbuttons_len = str(len(addbuttons))
        self.impwait()
        assert addbuttons_len in self.driver.find_element_by_xpath(self.itemstopcartXpath).text

    def clickfirstaddtobasket(self):
        self.driver.find_elements_by_class_name(self.addtobasketbuttonsClass).__getitem__(1).click()
        list = self.driver.find_elements_by_class_name(self.addtobasketbuttonsClass)
        print(len(list))

    def clicksecondaddtobasket(self):
        self.driver.find_elements_by_class_name(self.addtobasketbuttonsClass).__getitem__(2).click()

    #def updatequantity():

    #def changequantityfirstsku():

    #def changequantitysecondsku():

    #def addalltobasket():

    #def clickfirstfrequentitem():

    #def clickfirstalsoboughtitem():

    #def addtowishlist():
