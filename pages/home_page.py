from selenium.webdriver.common.by import By
import random as rd
from base_page import BasePage


class HomePage(BasePage):
    LIST_ITEMS_TO_ADD = (By.CSS_SELECTOR, ".inventory_item button")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    
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