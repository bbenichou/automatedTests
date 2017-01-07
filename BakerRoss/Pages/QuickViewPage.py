from Pages.listingpage import ListingPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class QuickView(ListingPage):

    # Variables
    iframeid = "fancybox-frame"
    quickviewid = "product_addtocart_form"
    firstBoxPPimgXpath = "//*[@id='page']/div[4]/div/div[4]/div[5]/div[6]/ul[1]/li[1]/a[1]/img"

    # Assertions

    # Locators

    # Actions
    def openquickview(self):
        ListingPage.gotolistingpage(self)
        self.driver.find_element_by_xpath(self.firstBoxPPimgXpath).click()

    def assertquickviewopen(self):
        self.driver.switch_to_frame(self.driver.find_element_by_id(self.iframeid))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.quickviewid)))
        self.driver.switch_to_default_content()