from Tests.loginTest import *
from Tests.ProdPageTest import *
from Tests.ConfirmationPopUpTest import *
from Tests.QuickviewTest import *
from TestsConfiguration import HTMLTestRunner

class SuiteAll(BasePage):
    #define testloader variable for each tests
    test1 = unittest.TestLoader().loadTestsFromTestCase(Login)
    test2 = unittest.TestLoader().loadTestsFromTestCase(productpage)
    test3 = unittest.TestLoader().loadTestsFromTestCase(confirmationpop)
    test4 = unittest.TestLoader().loadTestsFromTestCase(Quick)

    #group all tests variable into a suite
    all_tests = unittest.TestSuite([test1,test2,test3,test4])

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
    BasePage.driver.quit()