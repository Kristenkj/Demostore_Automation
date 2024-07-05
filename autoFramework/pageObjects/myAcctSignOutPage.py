from extensions.SeleniumExtended import SeleniumExtended
from pageObjects.locators.MyAcctSignOutLocator import MyAcctSignOutLocator
import logging as logger
from utils.BaseClass import BaseClass
from utils.helpers.config_helpers import get_base_url


class MyAcctSignOut(MyAcctSignOutLocator, BaseClass):

    endpoint = '/my-account'
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_acct(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to: {my_account_url}")
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(username, self.LOGIN_USER_NAME)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(password, self.LOGIN_PASSWORD)

    def click_login_button(self):
        logger.debug("Clicking 'Login' button.")
        self.sl.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_message_is_displayed(self, expect_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, expect_err)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.RIGISTER_PASSWORD,password)

    def click_register_button(self):
        logger.debug("Clicking 'Register' button.")
        self.sl.wait_and_click(self.REGISTER_BTN)


