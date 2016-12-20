from __future__ import print_function
from selenium import webdriver

driver=webdriver.Chrome("C:\\seleniumDriver\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://10.66.16.143:3000/dashboard/db/private-competitors-firstview-render")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/form/div[1]/ul/li[2]/input").send_keys("bengrafana")
driver.find_element_by_id("inputPassword").send_keys("badhorse2015")
driver.implicitly_wait(5)
driver.find_element_by_css_selector("body > div > div.main-view.ng-scope > div > div > div.login-inner-box > form > div.login-submit-button-row > button").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/div/div/ul[2]/li[2]/grafana-simple-panel/div/form/ul/li[2]/a").click()
driver.implicitly_wait(5)
driver.find_element_by_css_selector("body > div > div.main-view.ng-scope > div > div.ng-scope > div > div > div > ul.nav.pull-right > li.ng-scope > grafana-simple-panel > div > form > ul > li.dropdown.open > ul > li:nth-child(9) > a").click()
driver.implicitly_wait(1)
elementtest = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div[1]/div/div[2]/div[1]/panel-loader/grafana-panel-graph/grafana-panel/div/div[2]/ng-transclude/div[1]/div[2]/section/div[1]/div[2]/a").text
#elementtestval = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div/div[2]/div[1]/panel-loader/grafana-panel-graph/grafana-panel/div/div[2]/ng-transclude/div[1]/div[2]/section/div[1]/div[3]").text
print(elementtest)
#line = str("%s;%s" % elementtest, elementtestval)
#f1 = open('L:\\Work\\testfile.csv', 'w+')
#print(line, file=f1)
driver.quit()
