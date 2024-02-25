
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import Select

import time

class SeleniumExtended:


#### sets the default timeout to 10 seconds
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10
####

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout # If a timeout value is provided when calling the wait_and_input_text method, the timeout parameter will be used. Otherwise, the default_timeout value will be used.

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout # If a timeout value is provided when calling the wait_and_input_text method, the timeout parameter will be used. Otherwise, the default_timeout value will be used.
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except StaleElementReferenceException: # when the element is not attached to the DOM. In defferenct words, the element (button) is rloading or changing and is not clickable yet.
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout # If a timeout value is provided when calling the wait_and_input_text method, the timeout parameter will be used. Otherwise, the default_timeout value will be used.

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f'Element with locator = {locator}, does not contain text: "{text}", after waiting {timeout} seconds.'
        )

    def wait_until_element_is_visible(self, locator_or_element, timeout=None):
        timeout = timeout if timeout else self.default_timeout # If a timeout value is provided when calling the wait_and_input_text method, the timeout parameter will be used. Otherwise, the default_timeout value will be used.

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator_or_element),
            message=f'Element with locator = {locator_or_element}, is not visible after waiting {timeout} seconds.'
        )
    
        if isinstance(locator_or_element, tuple):
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator_or_element)
            )
        else:
            import selenium.webdriver.remote.webelement
            if isinstance(locator_or_element, selenium.webdriver.remote.webelement.WebElement):
                elem = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of(locator_or_element)
                )
            else:
                raise TypeError(f"The locator to check visibility must be a 'tuple' or a 'WebElement'. It was {type(locator_or_element)}")

        return elem

    def wait_until_elements_are_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout # If a timeout value is provided when calling the wait_and_input_text method, the timeout parameter will be used. Otherwise, the default_timeout value will be used.

        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

        return elem

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout # If a timeout value is provided when calling the wait_and_input_text method, the timeout parameter will be used. Otherwise, the default_timeout value will be used.
        err = err if err else f"Unable to find elements located by '{locator}'," \
                              f"after timeout of {timeout}"
                              
       # creating a custom error message if the err parameter is not provided
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)

        return elements

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout # If a timeout value is provided when calling the wait_and_input_text method, the timeout parameter will be used. Otherwise, the default_timeout value will be used.
        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = elm.text

        return element_text

    def wait_until_url_contains(self, url_substring, timeout=None):
        timeout = timeout if timeout else self.default_timeout # If a timeout value is provided when calling the wait_and_input_text method, the timeout parameter will be used. Otherwise, the default_timeout value will be used.

        elem = WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_substring)
        )

    def wait_and_select_dropdown(self, locator, to_select, select_by='visible_text'):
        """

        :param locator:
        :param to_select:
        :param select_by: Options are 'visible_text', 'index', or value 'value'
        :return:
        """

        select_element = self.wait_until_element_is_visible(locator)
        select = Select(select_element)
        if select_by.lower() == 'visible_text':
            select.select_by_visible_text(to_select)
        elif select_by.lower() == 'index':
            select.select_by_index(to_select)
        elif select_by.lower() == 'value':
            select.select_by_value(to_select)
        else:
            raise Exception(f"Invalid option for 'to_select' parameter. Valid values are 'visible_text', 'index', or value 'value'.")