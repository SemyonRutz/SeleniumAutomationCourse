from selenium.webdriver.common.by import By

class CheckoutPageLocators:
    FIRST_NAME = (By.ID, 'billing_first_name')
    LAST_NAME = (By.ID, 'billing_last_name')
    COMPANY_NAME = (By.ID, 'billing_company')
    STREET_ADDRESS_1 = (By.ID, 'billing_address_1')
    STREET_ADDRESS_2 = (By.ID, 'billing_address_2')
    CITY = (By.ID, 'billing_city')
    ZIP_CODE = (By.ID, 'billing_postcode')
    PHONE = (By.ID, 'billing_phone')
    EMAIL = (By.ID, 'billing_email')

    CHECKOUT_BTN = (By.ID, 'place_order')