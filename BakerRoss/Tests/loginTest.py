from Pages.LoginPage import *

class login(unittest.TestCase):
    def test_login(self):

        # go to the login page
        gotourl(path)
        impwait()

        # type email and password then click on the login button
        inputemail()
        inputpass()
        clicklogin()

        # Check if loggedin
        assertloggedin()

        # Logout
        logout()
        impwait()

        # Check if the username is not showing
        assertloggedout()
