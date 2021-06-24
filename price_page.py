"""
Functions for working with catalog
"""


from base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    """
    Stores elements locations
    """
    KATALOG_BUTTON = (By.CSS_SELECTOR, 'li:nth-of-type(1) > .b-main-navigation__link > .b-main-navigation__text')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[name="query"]')
    FRAME_PRICE = (By.CSS_SELECTOR, 'li:nth-of-type(1) .product__price-value.product__price-value_primary > span')
    FRAME = (By.CLASS_NAME, 'modal-iframe')
    PAGE_PRICE = (By.CSS_SELECTOR, '.offers-description__price.offers-description__price_primary')


class OnlinerHelper(BasePage):
    """
    Functions for operating the page
    """
    def enter_сatalog(self):
        """
        Enters сatalog
        """
        return self.find_element(SearchLocators.KATALOG_BUTTON, time=2).click()

    def find_in_catalog(self, item_to_find):
        """
        Finds provided item in catalog
        """
        return self.find_element(SearchLocators.SEARCH_FIELD, time=2).send_keys(item_to_find)

    def find_price(self):
        """
        Finds price of good in frame
        """
        return self.find_element(SearchLocators.FRAME_PRICE, time=5)

    def show_details(self):
        """
        Switches to the product page
        """
        return self.find_element(SearchLocators.FRAME_PRICE, time=5).click()

    def find_frame(self):
        """
        Finds iframe
        """
        return self.find_element(SearchLocators.FRAME, time=5)

    def switch(self, frame):
        """
        Switches to the frame
        """
        self.browser.switch_to.frame(frame)

    def default(self):
        """
        Switches to the default page
        """
        self.browser.switch_to.default_content()

    def find_price_in_page(self):
        """
        Finds price in the product page
        """
        return self.find_element(SearchLocators.PAGE_PRICE, time=2).text
