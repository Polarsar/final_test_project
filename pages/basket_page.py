from .base_page import BasePage
from pages.locators import BasketPageLocators
from .locators import BasketPageLocators

print("BasketPageLocators attributes:", dir(BasketPageLocators))

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not presented"



