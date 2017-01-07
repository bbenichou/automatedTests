from BasePageStructure.Base_page_structure import *
from Pages.ConfirmationpopuPage import *

class ProductPage(BasePage):

    # Variables
    listingPagePath = ("/arts-and-crafts")
    iframeid = "fancybox-frame"

    # Locators
    addtobasketbuttonsClass = "btn-cart"
    itemstopcartXpath = "//*[@id='cartHeader']/span"
    firstBoxPPimgXpath = "//*[@id='page']/div[4]/div/div[4]/div[5]/div[6]/ul[1]/li[1]/a[1]/img"
    firstBoxPPlinkXpath = "//*[@id='page']/div[4]/div/div[4]/div[5]/div[6]/ul[1]/li[1]/div[2]/form/a"
    megamenufirstlinkXpath = "//*[@id='custommenu-nav']/li[1]/a[1]"
    continueshoppingbuttonXpath = "//*[@id='quickorder-continue-link']/span"

    # Assertions

    # Actions
    def gotoprodurl(self):
        url = self.getdomain()
        self.driver.get(url)
        self.driver.maximize_window()
        self.impwait()
        self.driver.find_element_by_xpath(self.megamenufirstlinkXpath).click()
        self.impwait()
        firstBoxPP = self.driver.find_element_by_xpath(self.firstBoxPPimgXpath)
        hover = ActionChains(self.driver).move_to_element(firstBoxPP)
        hover.perform()
        self.driver.find_element_by_xpath(self.firstBoxPPlinkXpath).click()
        self.impwait()

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
