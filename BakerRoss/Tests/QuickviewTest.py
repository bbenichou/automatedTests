from Pages.QuickViewPage import *
import unittest


class Quick(unittest.TestCase, QuickView):

    def test_quickview(self):

        BasePage.gotolistingpage(self)
        QuickView.openquickview(self)
        QuickView.assertquickviewopen(self)