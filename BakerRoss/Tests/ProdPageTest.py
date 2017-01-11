from Pages.ProductPage import *
import unittest


class productpage(unittest.TestCase, ProductPage):

    def test_productpage(self):

        #go to the product page
        BasePage.gotoprodurl(self)

        # add each sku to the basket and check if the top cart is updated
        ProductPage.addtobasket(self)
        ProductPage.assertaddtobasket(self)

