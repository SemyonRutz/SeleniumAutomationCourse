import pytest, time
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.configs.generic_configs import GenericConfigs
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.OrderConfirmation import OrderConfirmation
# from ssqatest.src.helpers.db_helper.get_order_from_db_by_order_number import get_order_from_db_by_order_number

@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckOutUser:

    
    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):

        # go to home page
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_confirmation_p = OrderConfirmation(self.driver)

        home_p.go_to_home_page()

        # add one item to cart
        home_p.click_first_add_to_cart_button()

        # wait for the cart to show 1 item
        header.wait_until_count_item_cpunt('1 item')

        # go to cart
        header.click_on_cart_right_header()

        # verify products in the cart
        product_names = cart_p.get_all_products_names_in_cart()
        assert len(product_names) == 1, f'Expected 1 product in the cart. Actual: {len(product_names)}'

        # apply a coupon
        coupon_code = GenericConfigs.FREE_COUPON # get coupon from config file
        cart_p.apply_coupon(coupon_code)

        # verify coupon is applied
        cart_p.get_coupon_in_totals_text(f'Coupon: {coupon_code}')

        # click on checkout
        time.sleep(2)
        cart_p.click_on_checkout()

        # fill in billing information
        first_name = GenericConfigs.FIRST_NAME
        last_name = GenericConfigs.LAST_NAME
        company_name = GenericConfigs.COMPANY_NAME
        street_address_1 = GenericConfigs.STREET_ADDRESS_1
        street_address_2 = GenericConfigs.STREET_ADDRESS_2
        city = GenericConfigs.CITY
        zip = GenericConfigs.ZIP_CODE
        phone = GenericConfigs.PHONE
        checkout_p.fill_in_billing_information(first_name, last_name, company_name, street_address_1, street_address_2, city, zip, phone)

        
        # click on palce order
        checkout_p.click_on_place_order_btn()

        # verify order is received
        order_confirmation_p.get_order_confirmation_text()

        # verify order number is displayed
        order_number = order_confirmation_p.get_order_number()
        print('****************************************************************************************************')
        print(f'Order number: {order_number}')
        print('****************************************************************************************************')


        # # verify order is recorded in the database (via SQL or via API)
        # db_order = get_order_from_db_by_order_number(order_number)
        # assert db_order, f'Order number {order_number} not found in the database'

        
        # pdb
        # import pdb; pdb.set_trace()