from BasePage.Base_page_structure import *
from Pages.Confirmationpopup import *

# Variables
#addtobasketbuttons = driver.find_elements_by_class_name("btn-cart").next()
listingPageUrl = ("http://www.bakerross.co.uk/arts-and-crafts")

# Locators
firstBoxPPimgXpath = "//*[@id='page']/div[4]/div/div[4]/div[5]/div[6]/ul[1]/li[1]/a[1]/img"
firstBoxPPlinkXpath = "//*[@id='page']/div[4]/div/div[4]/div[5]/div[6]/ul[1]/li[1]/div[2]/form/a"
addtobasketbuttonsClass = "btn-cart"

# Assertions


# Actions

def gotoprodurl():
    driver.get(listingPageUrl)
    driver.maximize_window()
    impwait()
    firstBoxPP = driver.find_element_by_xpath(firstBoxPPimgXpath)
    hover = ActionChains(driver).move_to_element(firstBoxPP)
    hover.perform()
    driver.find_element_by_xpath(firstBoxPPlinkXpath).click()
    impwait()

def clickfirstaddtobasket():
    driver.find_elements_by_class_name(addtobasketbuttonsClass).__getitem__(1).click()

def clicksecondaddtobasket():
    driver.find_elements_by_class_name(addtobasketbuttonsClass).__getitem__(2).click()

#def updatequantity():

#def changequantityfirstsku():

#def changequantitysecondsku():

#def addalltobasket():

#def clickfirstfrequentitem():

#def clickfirstalsoboughtitem():

#def addtowishlist():
