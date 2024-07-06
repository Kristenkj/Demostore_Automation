import time

import pytest
from configs.generic_configs import GenericConfigs
from pageObjects.Header import Header
from pageObjects.cartPage import CartPage
from pageObjects.homePage import homePage
from utils.BaseClass import BaseClass
from pageObjects.checkOutPage import CheckoutPage
from pageObjects.locators import HomePageLocators
from pageObjects.orderReceivedPage import OrderReceivedPage

class TestEndToEndCheckoutGuestUser(BaseClass):

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        # Go to home page
        home_p = homePage(self.driver)

        #home_p.go_to_home_page() #Not needed because of BaseClass
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceivedPage(self.driver)
        # Add 1 item to cart
        home_p.click_first_item_add_to_cart_btn()

        # Make sure the cart is updated before going to cart
        #header.wait_until_cart_item_count(1) #Use if computer/selenium is moving really fast

        # Go to cart
        header.click_on_cart_on_right_header()

        # Verify that there is one item in the cart
        product_names = cart_p.get_all_product_names_in_cart()
        assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)} "

        # Apply free coupon
        coupon_code = GenericConfigs.FREE_COUPON
        #cart_p.apply_coupon(coupon_code)

        # Click on proceed to checkout
        cart_p.click_on_proceed_to_check_out()

        # Fill in forms
        checkout_p.fill_in_billing_info()

        checkout_p.click_to_show_coupon_billing()
        checkout_p.input_billing_coupon_code(coupon_code)
        checkout_p.click_on_apply_coupon_billing()

        #Click on free shipping
        checkout_p.click_on_free_shipping()

        # Click on place order
        checkout_p.click_place_order()

        # Verify order is received
        order_received_p.verify_order_received_page_loaded()



    #time.sleep(3)
