from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID,"user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID,"login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
    
    def get_error_message(self):
        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return message.text
    
    def enter_username(self, username):
        self.find(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.find(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.click_when_clickable(*self.LOGIN_BUTTON)

    def is_login_btn_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGIN_BUTTON)
            )
            return True
        except:
            return False

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()            