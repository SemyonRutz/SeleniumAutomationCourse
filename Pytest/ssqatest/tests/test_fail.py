import pytest
from ssqatest.src.pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.fail
    def test_fail(self):

        home_p = HomePage(self.driver)
        home_p.go_to_home_page()    
        assert False, "Failing test on purpose"
        
