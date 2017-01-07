from Pages.ConfirmationpopuPage import *
import unittest

class confirmation(unittest.TestCase, ConfirmationPopUp):
    def test_confirmationpopup(self):

        #
        ConfirmationPopUp.openconfirmationpopuponeitem(self)

        #
        ConfirmationPopUp.assertconfirmoneitem(self)

        #
        ConfirmationPopUp.closeconfirmationpopup(self)