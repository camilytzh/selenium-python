import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.headless = False

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()

    yield driver
    driver.quit()