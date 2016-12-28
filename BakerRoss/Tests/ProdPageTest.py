from Pages.ProductPage import *

class productpage(unittest.TestCase):
    def test_productpage(self):

        #go to the product page
        gotoprodurl()

        # add each sku to the basket and check if the top cart is updated
        addtobasket()
        assertaddtobasket()

