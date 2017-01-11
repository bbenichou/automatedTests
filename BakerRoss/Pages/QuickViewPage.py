from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from BasePageStructure.Base_page_structure import BasePage


class QuickView(BasePage):

    # Variables
    iframeid = "fancybox-frame"
    quickviewid = "product_addtocart_form"
    firstBoxPPimgXpath = BasePage.firstBoxPPimgXpath
    productdetailslinkxpath = "//*[@id='product_addtocart_form']/div[3]/div[6]/a"

    # Assertions

    # Locators

    # Actions
    def openquickview(self):
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.firstBoxPPimgXpath)))
        self.driver.find_element_by_xpath(self.firstBoxPPimgXpath).click()

    def assertquickviewopen(self):
        self.driver.switch_to_frame(self.driver.find_element_by_id(self.iframeid))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.quickviewid)))
        self.driver.switch_to_default_content()

    def clickproductdetails(self):
        self.driver.switch_to_frame(self.driver.find_element_by_id(self.iframeid))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.productdetailslinkxpath)))
        self.driver.find_element_by_xpath(self.productdetailslinkxpath).click()
