from BasePageStructure.Base_page_structure import *
from Pages.Confirmationpopup import *

# Variables
listingPagePath = ("/arts-and-crafts")

# Locators
addtobasketbuttonsClass = "btn-cart"
itemstopcartXpath = "//*[@id='cartHeader']/span"
firstBoxPPimgXpath = "//*[@id='page']/div[4]/div/div[4]/div[5]/div[6]/ul[1]/li[1]/a[1]/img"
firstBoxPPlinkXpath = "//*[@id='page']/div[4]/div/div[4]/div[5]/div[6]/ul[1]/li[1]/div[2]/form/a"
megamenufirstlinkXpath = "//*[@id='custommenu-nav']/li[1]/a[1]"

# Assertions


# Actions
def gotoprodurl():
    getdomain()
    url = getdomain()
    driver.get(url)
    driver.maximize_window()
    impwait()
    driver.find_element_by_xpath(megamenufirstlinkXpath).click()
    impwait()
    firstBoxPP = driver.find_element_by_xpath(firstBoxPPimgXpath)
    hover = ActionChains(driver).move_to_element(firstBoxPP)
    hover.perform()
    driver.find_element_by_xpath(firstBoxPPlinkXpath).click()
    impwait()

def addtobasket():
    addbuttons = driver.find_elements_by_class_name(addtobasketbuttonsClass)
    addbuttons_len = len(addbuttons)
    for i in range(0,addbuttons_len):
        driver.find_elements_by_class_name(addtobasketbuttonsClass).__getitem__(i).click()
        closeconfirmationpopup()
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
