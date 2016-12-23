from Pages.ProductPage import *

# Variables


# go to the product page
gotoprodurl()

# add each sku to the basket and check if the top cart is updated
addtobasket()
assertaddtobasket()

# Quit
driver.quit()
