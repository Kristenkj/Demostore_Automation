from pageObjects.locators.MyAccountSignedInLocators import MyAccountSignedInLocators
from extensions.SeleniumExtended import SeleniumExtended

class MyAcctSignIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
        self.sl.wait_until_elements_is_visible(self.LEFT_NAV_LOGOUT_BTN)





