from utils.helpers.config_helpers import get_base_url
from extensions.SeleniumExtended import SeleniumExtended
from pageObjects.locators.HomePageLocators import HomePageLocators

class homePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_first_item_add_to_cart_btn(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)




