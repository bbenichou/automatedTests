from Pages.LoginPage import *
import unittest

class Login(unittest.TestCase, LoginPage):

    def test_login(self):
        # go to the login page
        BasePage.gotourl(self, LoginPage.path)
        BasePage.impwait(self)

        # type email and password then click on the login button
        LoginPage.inputemail(self)
        LoginPage.inputpass(self)
        LoginPage.clicklogin(self)

        # Check if loggedin
        LoginPage.assertloggedin(self)

        # Logout
        LoginPage.logout(self)
        LoginPage.impwait(self)

        # Check if the username is not showing
        LoginPage.assertloggedout(self)
