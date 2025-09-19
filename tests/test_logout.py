from utils.data_loader import DataLoader
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_logout_user(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    data = DataLoader.load_json("users.json")["valid_user"]

    login_page.open()
    login_page.login(data["username"], data["password"])
    assert home_page.is_title_visible()

    home_page.logout()
    assert login_page.is_login_btn_visible()
