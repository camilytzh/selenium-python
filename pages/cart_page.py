from selenium.webdriver.common.by import By
import random as rd
from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    LIST_REMOVE_BUTTON_CART = (By.CSS_SELECTOR, ".item_pricebar button")
    LIST_CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")

    def checkout(self):
        self.click_when_clickable(*self.CHECKOUT_BUTTON)

    def remove_items(self, number_of_items):
        items = self.finds(*self.LIST_REMOVE_BUTTON_CART)
        total_items_in_cart = len(items)

        if number_of_items > total_items_in_cart:
            raise ValueError(f"There are only: {total_items_in_cart} items available.")
        
        for _ in range(number_of_items):
            item_to_remove = rd.choice(items)
            self.click_element_when_clickable(item_to_remove)
            items.remove(item_to_remove) #Avoid to choose the same item

    def is_cart_empty(self):
        items = self.driver.find_elements(*self.LIST_CART_ITEMS)
        if len(items) == 0:
            return True