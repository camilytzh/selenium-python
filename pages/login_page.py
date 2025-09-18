from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID,"user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID,"login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
    
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()            