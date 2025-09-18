from base_page import BasePage
from selenium.webdriver.common.by import By

class OverviewPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def click_finish_button(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()