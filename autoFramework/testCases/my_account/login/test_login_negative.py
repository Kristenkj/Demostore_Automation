import pytest
from pageObjects.myAcctSignOutPage import MyAcctSignOut
from utils.BaseClass import BaseClass


class TestLoginNegative(BaseClass):

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        # go to my acct
        my_account = MyAcctSignOut(self.driver)
        my_account.go_to_my_acct()
        # Type username
        my_account.input_login_username("thfyrg")
        # type password
        my_account.input_login_password("hsfgskjf")
        # click login
        my_account.click_login_button()
        #verify error message
        #expected_error = 'ERROR: Invalid username. Lost your password?'
        #my_account.wait_until_error_message_is_displayed(expected_error)
