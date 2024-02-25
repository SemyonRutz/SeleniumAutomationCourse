from selenium.webdriver.common.by import By

class HeaderLocators:
    
    CART_RIGHT_HEADER = (By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-7 > a')
    COUNT_TEXT = (By.CSS_SELECTOR, 'ul#site-header-cart span.count')