from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class OverviewPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def click_finish_button(self):
        self.click_when_clickable(*self.FINISH_BUTTON)