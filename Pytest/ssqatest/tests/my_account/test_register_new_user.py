import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.helpers.generic_helpers import generate_tandom_email_and_password


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_new_user(self):
        pass

        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)
        my_account_o.go_to_my_account()
 
        rand_email = generate_tandom_email_and_password() # reutrns a dictionary with email and password

        my_account_o.input_register_email(rand_email['email'])
        my_account_o.input_register_password(rand_email['password'])
        my_account_o.click_register_button()
        
        # verify user is registered 
        my_account_i.verify_user_is_signed_in()
        

