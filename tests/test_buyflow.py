from utils.data_loader import DataLoader
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.complete_checkout_page import CompleteCheckoutPage

def test_complete_buyflow(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    overview_page = OverviewPage(driver)
    complete_checkout_page = CompleteCheckoutPage(driver)
    data = DataLoader.load_json("users.json")["valid_user"]

    login_page.open()
    login_page.login(data["username"], data["password"])
    assert home_page.is_title_visible()

    home_page.add_to_cart_items(3)
    home_page.go_shopping_cart()
    cart_page.checkout()
    checkout_page.fill_checkout_form("Mary", "Jones", "2222")
    overview_page.click_finish_button()
    actual_text = complete_checkout_page.get_success_message_text()
    expected_text = "Thank you for your order!"

    assert actual_text in expected_text