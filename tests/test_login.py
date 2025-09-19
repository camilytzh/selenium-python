from utils.data_loader import DataLoader
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_valid_user(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    data = DataLoader.load_json("users.json")["valid_user"]

    login_page.open()
    login_page.login(data["username"], data["password"])
    assert home_page.is_title_visible()

def test_login_invalid_user(driver):
    login_page = LoginPage(driver)
    data = DataLoader.load_json("users.json")["invalid_user"]

    login_page.open()
    login_page.login(data["username"], data["password"])

    expected_text = "Epic sadface: Username and password do not match any user in this service"
    actual_text = login_page.get_error_message()
    

    assert actual_text in expected_text

def test_locked_user(driver):
    login_page = LoginPage(driver)
    data = DataLoader.load_json("users.json")["locked_user"]

    login_page.open()
    login_page.login(data["username"], data["password"])
    
    expected_text = "Epic sadface: Sorry, this user has been locked out."
    actual_text = login_page.get_error_message()
    
    assert actual_text in expected_text
