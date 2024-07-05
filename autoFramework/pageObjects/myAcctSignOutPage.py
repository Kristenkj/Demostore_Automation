from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from autoFramework.SeleniumExtended import SeleniumExtended
from pageObjects.locators.MyAcctSignOutLocator import MyAcctSignOutLocator
from utils.BaseClass import BaseClass


class MyAcctSignOut(MyAcctSignOutLocator, BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    def go_to_my_acct(self):
        self.driver.get('https://demostore.supersqa.com/my-account/')

    def input_login_username(self, username):
        self.sl.wait_and_input_text(username, self.LOGIN_USER_NAME)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(password, self.LOGIN_PASSWORD)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BTN)
