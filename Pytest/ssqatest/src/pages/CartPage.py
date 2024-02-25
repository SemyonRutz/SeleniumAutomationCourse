from selenium.webdriver.common.keys import Keys
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        pass

    def get_all_products_names_in_cart(self):
        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_name_elements]
        return product_names

    def apply_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FIELD, coupon_code)
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def get_coupon_in_totals_text(self, coupon_text):
        return self.sl.wait_until_element_contains_text(self.COUPON_IN_TOTALS, coupon_text)

    def click_on_checkout(self):
        self.sl.wait_and_click(self.CHECKOUT_BTN)