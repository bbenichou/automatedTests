from selenium import webdriver

driver=webdriver.Chrome("C:\\seleniumDriver\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.bakerross.co.uk/customer/account/login/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_id("email").send_keys("b.benichou@bakerross.co.uk")
driver.find_element_by_id("pass").send_keys("testtest")
driver.find_element_by_xpath("//*[@id='send2']/span/span").click()
driver.implicitly_wait(5)
assert "Ben" in driver.find_element_by_xpath("//*[@id='page']/div[4]/div/div[3]/div[2]/div/div[2]/h2").text
driver.find_element_by_xpath("//*[@id='page']/div[1]/div/ul[2]/li[2]/a").click()
driver.implicitly_wait(5)
driver.quit()
