import math
import re
import time
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def solve_quiz_and_get_code(self):
        try:
            time.sleep(0.5)
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Alert text: {alert_text}")

            x_match = re.search(r"x\s*=\s*([0-9.+-eE]+)", alert_text)
            if not x_match:
                raise Exception("Не удалось найти число x в алерте")

            x_val = float(x_match.group(1))
            answer = str(math.log(abs(12 * math.sin(x_val))))

            alert.send_keys(answer)
            alert.accept()

            time.sleep(1)
            alert = self.browser.switch_to.alert
            print(f"Код подтверждения из alert: {alert.text}")
            alert.accept()

        except NoAlertPresentException:
            print("Alert не найден")
        except Exception as e:
            print(f"Ошибка при решении капчи: {e}")

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()



