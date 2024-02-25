from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By

def Verify_16_products_are_displayed():
    """
    Returns

    """

    selenium_lib = BuiltIn().get_library_instance('SeleniumLibrary') # this is the instance of the SeleniumLibrary
    browser = selenium_lib.driver # this is the instance of the browser

    import time

    # get the number of products displayed
    all_product_elements = browser.find_elements(By.CSS_SELECTOR, 'li.product.type-product')


    if len(all_product_elements) != 16:
        raise Exception('16 products are not displayed')

    # check if the product names are displayed
    logger.info('checking if the product names are displayed')
    for product_element in all_product_elements:
        if not product_element.is_displayed():
            raise Exception('Product names are not displayed')

    logger.info('PASS. Correct number of products are displayed')