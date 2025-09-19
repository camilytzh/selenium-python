from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def enter_first_name(self, first_name):
        self.find(*self.FIRST_NAME_INPUT).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.find(*self.LAST_NAME_INPUT).send_keys(last_name)

    def enter_zip_code(self, zip_code):
        self.find(*self.ZIP_CODE_INPUT).send_keys(zip_code)

    def click_continue(self):
        self.click_when_clickable(*self.CONTINUE_BUTTON)

    def fill_checkout_form(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
        self.click_continue()        