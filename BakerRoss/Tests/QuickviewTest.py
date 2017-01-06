from Pages.QuickView import *

class quickview(unittest.TestCase):
    def test_quickview(self):
        openquickview()
        assertquickviewopen()