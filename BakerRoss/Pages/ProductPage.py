from BasePage.Base_page_structure import *
from Pages.Confirmationpopup import *

# Variables
listingPagePath = ("/arts-and-crafts")

# Locators
addtobasketbuttonsClass = "btn-cart"
itemstopcartXpath = "//*[@id='cartHeader']/span"

# Assertions


# Actions
def addtobasket():
    addbuttons = driver.find_elements_by_class_name(addtobasketbuttonsClass)
    addbuttons_len = len(addbuttons)
    for i in range(0,addbuttons_len):
        driver.find_elements_by_class_name(addtobasketbuttonsClass).__getitem__(i).click()
        confpopupclickcontinueshopping()
        driver.switch_to_default_content()

def assertaddtobasket():
    addbuttons = driver.find_elements_by_class_name(addtobasketbuttonsClass)
    addbuttons_len = str(len(addbuttons))
    impwait()
    assert addbuttons_len in driver.find_element_by_xpath(itemstopcartXpath).text

def clickfirstaddtobasket():
    driver.find_elements_by_class_name(addtobasketbuttonsClass).__getitem__(1).click()
    list = driver.find_elements_by_class_name(addtobasketbuttonsClass)
    print(len(list))

def clicksecondaddtobasket():
    driver.find_elements_by_class_name(addtobasketbuttonsClass).__getitem__(2).click()

#def updatequantity():

#def changequantityfirstsku():

#def changequantitysecondsku():

#def addalltobasket():

#def clickfirstfrequentitem():

#def clickfirstalsoboughtitem():

#def addtowishlist():
