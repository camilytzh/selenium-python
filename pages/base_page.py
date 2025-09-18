from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.timeout = timeout

    def click_when_clickable(self, by, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def find(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def finds(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located((by, locator))
        )