from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    BILLING_FIRST_NAME_FIELD = (By.ID, 'billing_first_name')
    BILLING_LAST_NAME_FIELD = (By.ID, 'billing_last_name')
    BILLING_ADDRESS_1_FIELD = (By.ID, 'billing_address_1')
    BILLING_CITY_FIELD = (By.ID, 'billing_city')
    BILLING_ZIP_FIELD = (By.ID, 'billing_postcode')
    BILLING_PHONE_FIELD = (By.ID, 'billing_phone')
    BILLING_EMAIL_FIELD = (By.ID, 'billing_email')

    PLACE_ORDER_BTN = (By.ID, 'place_order')

    BILLING_FREE_SHIPPING_RADIO = (By.ID, 'shipping_method_0_free_shipping1')
    BILLING_COUPON_FIELD = (By.ID, 'coupon_code')
    BILLING_APPLY_COUPON_BTN = (By.NAME, "apply_coupon")

    CLICK_HERE_TO_ENTER_COUPON_BILLING = (By.CSS_SELECTOR, "a[class=showcoupon]")