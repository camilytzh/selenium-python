from selenium.webdriver.common.by import By
import random as rd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage


class HomePage(BasePage):
    LIST_ITEMS_TO_ADD = (By.CSS_SELECTOR, ".inventory_item button")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    BURGER_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    
    def get_products_title_element(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCTS_TITLE)
        )
        return element
    
    def add_to_cart_items(self, number_of_items):
        items = self.driver.find_elements(*self.LIST_ITEMS_TO_ADD)
        total_items = len(items)

        if number_of_items > total_items:
            raise ValueError(f"There are only: {total_items} items available.")
        
        for _ in range(number_of_items):
            selected_item = rd.choice(items)
            selected_item.click()
            items.remove(selected_item) #Avoid to choose the same item

    def go_shopping_cart(self):
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()

    def click_burger_button(self):
        self.driver.find_element(*self.BURGER_BUTTON).click()

    def click_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def logout(self):
        self.click_burger_button()
        self.click_logout_button()                