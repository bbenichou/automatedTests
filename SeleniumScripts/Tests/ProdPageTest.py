from Pages.ProductPage import *

# Variables
listingPageUrl = ("http://www.bakerross.co.uk/arts-and-crafts")
listingSalePageUrl = ("http://www.bakerross.co.uk/arts-and-crafts/sale")
listingNewPageUrl = ("http://www.bakerross.co.uk/arts-and-crafts/new")

# go to the product page
gotoprodurl()

# add each sku to the basket and check if the top cart is updated
addtobasket()
assertaddtobasket()


