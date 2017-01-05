#Import tests
from Tests.loginTest import *
from Tests.ProdPageTest import *
from TestsConfiguration import HTMLTestRunner

#define testloader variable for each tests
test1 = unittest.TestLoader().loadTestsFromTestCase(login)
test2 = unittest.TestLoader().loadTestsFromTestCase(productpage)

#group all tests variable into a suite
all_tests = unittest.TestSuite([test1,test2])

# run the suite with default unittest
#unittest.TextTestRunner(verbosity=2).run(all_tests)

#run the suite with htmltestrunner

outfile = open(localenv + '\\automatedTests\\BakerRoss\\TestSuite\\TestResults\\Report_testSuiteAll.html', "w")

runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Suite Report:  ALL test',
                description='Report Output.'
                )

runner.run(all_tests)

#close the browser
driver.quit()