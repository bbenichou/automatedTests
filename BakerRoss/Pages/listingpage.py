from BasePageStructure.Base_page_structure import *

class ListingPage(BasePage):

    # Variables

    # Assertions
    megamenufirstlinkXpath = "//*[@id='custommenu-nav']/li[1]/a[1]"

    # Locators

    # Actions
    def gotolistingpage(self):
        self.getdomain()
        url = self.getdomain()
        self.driver.get(url)
        self.driver.maximize_window()
        self.impwait()
        self.driver.find_element_by_xpath(self.megamenufirstlinkXpath).click()
        self.impwait()