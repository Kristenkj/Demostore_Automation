import pytest
from pageObjects.myAcctSignOutPage import MyAcctSignOut
from utils.BaseClass import BaseClass


class TestRegisterNewUser(BaseClass):

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):

        # Go to my account
        my_acct_o = MyAcctSignOut(self.driver)
        my_acct_o.go_to_my_acct()
        # Fill in email
        my_acct_o.input_register_email('christ@supersqa.com')
        # Fill in password
        my_acct_o.input_register_password('abd1234')
        #Click register
        my_acct_o.click_register_button()
        # Verify user is registered