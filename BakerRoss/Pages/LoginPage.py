from BasePageStructure.Base_page_structure import *


class LoginPage(BasePage):

    # Variables
    path = "/customer/account/login/"

    # Assertions
    nameAssert = "Ben"

    # Locators
    emailXpath = "//*[@id='email']"
    passXpath = "//*[@id='pass']"
    loginButtonXpath = "//*[@id='send2']/span/span"
    welcomeTextXpath = "//*[@id='page']/div[4]/div/div[3]/div[2]/div/div[2]/h2"
    logoutLinkXpath = "//*[@id='page']/div[1]/div/ul[2]/li[2]/a"
    headerUsernameXpath = "//*[@id='page']/div[1]/div/ul[1]/li[1]"

    # Methods
    def inputemail(self):
        email = BasePage.getloginvalue(self)
        self.driver.find_element_by_xpath(self.emailXpath).send_keys(email)

    def inputpass(self):
        password = BasePage.getpassvalue(self)
        self.driver.find_element_by_xpath(self.passXpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.loginButtonXpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.logoutLinkXpath).click()

    def assertloggedin(self):
        assert self.nameAssert in self.driver.find_element_by_xpath(self.headerUsernameXpath).text
        assert self.nameAssert in self.driver.find_element_by_xpath(self.welcomeTextXpath).text

    def assertloggedout(self):
        assert self.nameAssert not in self.driver.find_element_by_xpath(self.headerUsernameXpath).text
