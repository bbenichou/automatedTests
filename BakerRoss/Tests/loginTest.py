from Pages.LoginPage import *

class login(unittest.TestCase):

    def test_login(self):
        # go to the login page
        BasePage.gotourl(LoginPage.path)
        BasePage.impwait()

        # type email and password then click on the login button
        LoginPage.inputemail()
        LoginPage.inputpass()
        LoginPage.clicklogin()

        # Check if loggedin
        LoginPage.assertloggedin()

        # Logout
        LoginPage.logout()
        LoginPage.impwait()

        # Check if the username is not showing
        LoginPage.assertloggedout()
