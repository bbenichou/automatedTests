from LoginPageStructure import *

# go to the login page
gotourl(url)
impwait()

# type email and password then click on the login button
inputemail()
inputpass()
clicklogin()
impwait()

# Check if loggedin
assertloggedin()

# Logout
logout()
impwait()

# Check if the username is not showing
assertloggedout()

# Quit
driver.quit()
