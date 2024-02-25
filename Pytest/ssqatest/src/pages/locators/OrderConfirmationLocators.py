from selenium.webdriver.common.by import By

class OrderConfirmationLocators:
    
    ORDER_CONFIRMATION_TEXT = (By.CSS_SELECTOR, 'h1.entry-title')

    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.woocommerce-order-overview__order.order strong')

