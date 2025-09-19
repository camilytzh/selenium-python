from selenium.webdriver.common.by import By
import random as rd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    LIST_ITEMS_TO_ADD = (By.CSS_SELECTOR, ".inventory_item button")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    BURGER_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    
    def is_title_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCTS_TITLE)
            )
            return True
        except:
            return False
    
    def add_to_cart_items(self, number_of_items):
        items = self.finds(*self.LIST_ITEMS_TO_ADD)
        total_items = len(items)

        if number_of_items > total_items:
            raise ValueError(f"There are only: {total_items} items available.")
        
        for _ in range(number_of_items):
            selected_item = rd.choice(items)
            self.click_element_when_clickable(selected_item)
            items.remove(selected_item) #Avoid to choose the same item

    def go_shopping_cart(self):
        self.click_when_clickable(*self.SHOPPING_CART_LINK)

    def click_burger_button(self):
        self.click_when_clickable(*self.BURGER_BUTTON)

    def click_logout_button(self):
        self.click_when_clickable(*self.LOGOUT_BUTTON)

    def logout(self):
        self.click_burger_button()
        self.click_logout_button()                