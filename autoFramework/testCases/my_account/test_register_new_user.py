import pytest
from autoFramework.pageObjects.myAcctSignOutPage import MyAcctSignOut
from utils.BaseClass import BaseClass
from utils.helpers.generic_helpers import generate_random_email_and_password
from pageObjects.myAcctSignInPage import MyAcctSignIn
class TestRegisterNewUser(BaseClass):

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):

        # Go to my account
        my_acct_o = MyAcctSignOut(self.driver)
        my_acct_i = MyAcctSignIn(self.driver)
        my_acct_o.go_to_my_acct()
        # Fill in email
        random_email = generate_random_email_and_password()
        my_acct_o.input_register_email(random_email['email'])
        # Fill in password
        random_password = generate_random_email_and_password()
        my_acct_o.input_register_password(random_password['password'])
        #Click register
        my_acct_o.click_register_button()
        # Verify user is registered
        my_acct_i.verify_user_is_signed_in()
