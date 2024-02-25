from ssqatest.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.generic_helpers import generate_tandom_email_and_password

class CheckoutPage(CheckoutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    
    def fill_in_first_name(self, first_name):
        self.sl.wait_and_input_text(self.FIRST_NAME, first_name)
    
    def fill_in_last_name(self, last_name):
        self.sl.wait_and_input_text(self.LAST_NAME, last_name)
    
    def fill_in_company_name(self, company_name):
        self.sl.wait_and_input_text(self.COMPANY_NAME, company_name)

    def fill_in_street_address_1(self, street_address_1):     
        self.sl.wait_and_input_text(self.STREET_ADDRESS_1, street_address_1)

    def fill_in_street_address_2(self, street_address_2):
        self.sl.wait_and_input_text(self.STREET_ADDRESS_2, street_address_2)
    
    def fill_in_city(self, city):
        self.sl.wait_and_input_text(self.CITY, city)

    def fill_in_zip_code(self, zip):
        self.sl.wait_and_input_text(self.ZIP_CODE, zip)

    def fill_in_phone(self, phone):
        self.sl.wait_and_input_text(self.PHONE, phone)

    def fill_in_email(self, email=None):
        if not email:
            email = generate_tandom_email_and_password()['email']
        self.sl.wait_and_input_text(self.EMAIL, email)



    def fill_in_billing_information(self, first_name, last_name, company_name, street_address_1, street_address_2, city, zip, phone, email=None):
        self.fill_in_first_name(first_name)
        self.fill_in_last_name(last_name)
        self.fill_in_company_name(company_name)
        self.fill_in_street_address_1(street_address_1)
        self.fill_in_street_address_2(street_address_2)
        self.fill_in_city(city)
        self.fill_in_zip_code(zip)
        self.fill_in_phone(phone)
        self.fill_in_email(email)

    def click_on_place_order_btn(self):
        self.sl.wait_and_click(self.CHECKOUT_BTN)