from utils.data_loader import DataLoader
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

def test_empty_cart(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    data = DataLoader.load_json("users.json")["valid_user"]

    login_page.open()
    login_page.login(data["username"], data["password"])
    assert home_page.is_title_visible()

    home_page.add_to_cart_items(3)
    home_page.go_shopping_cart()
    cart_page.remove_items(3)

    assert cart_page.is_cart_empty()