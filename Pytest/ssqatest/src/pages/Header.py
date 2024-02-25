from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.HeaderLocators import HeaderLocators

class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    
    def click_on_cart_right_header (self):
        self.sl.wait_and_click(self.CART_RIGHT_HEADER)

    def wait_until_count_item_cpunt (self, text):
        self.sl.wait_until_element_contains_text(self.COUNT_TEXT, text)

    