from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_added_product_name(self, expected_name):
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert expected_name == added_name, f"Expected product name '{expected_name}', but got '{added_name}'"

    def should_be_basket_price_equal_product_price(self, expected_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert expected_price == basket_price, f"Expected basket price '{expected_price}', but got '{basket_price}'"


