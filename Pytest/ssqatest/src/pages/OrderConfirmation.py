from ssqatest.src.pages.locators.OrderConfirmationLocators import OrderConfirmationLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended

class OrderConfirmation(OrderConfirmationLocators):
        
        def __init__(self, driver):
            self.driver = driver
            self.sl = SeleniumExtended(self.driver)
        
        def get_order_confirmation_text(self):
            self.sl.wait_until_element_contains_text(self.ORDER_CONFIRMATION_TEXT, 'Order received')

        def get_order_number(self):
            return self.sl.wait_and_get_text(self.ORDER_NUMBER)