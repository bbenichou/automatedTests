#Import tests
from Tests.loginTest import *
from Tests.ProdPageTest import *

#define testloader variable for each tests
test1 = unittest.TestLoader().loadTestsFromTestCase(login)
test2 = unittest.TestLoader().loadTestsFromTestCase(productpage)

#group all tests variable into a suite
all_tests = unittest.TestSuite([test1,test2])

#run the suite
unittest.TextTestRunner(verbosity=2).run(all_tests)

#close the browser
driver.quit()