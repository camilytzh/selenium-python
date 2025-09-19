from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CompleteCheckoutPage(BasePage):
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def get_success_message_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )
        return element.text