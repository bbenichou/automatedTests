import unittest
from Pages.ListingProdPage import *
from Pages.QuickViewPage import *

class Feefo(unittest.TestCase, QuickView):

    def test_feefo(self):
        #go to a listing page with reviews
        BasePage.gotolistingpagereview(self, ListingPage.pathwithreview)

        #open a quick view popup
        QuickView.openquickview(self)

        #Assert stars are present

        #Go to product page
        QuickView.clickproductdetails(self)