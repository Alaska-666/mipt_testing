import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from users.user_generator import UserGenerator
from pages.login_page import LoginPage


@pytest.fixture
def user_is_logged_in():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    login_page = LoginPage(driver, wait)
    assert "Sign in to GitHub" in login_page.title

    login_page.full_authorization(UserGenerator.generate_from_json("users/testuser.json"))
    assert "Incorrect username or password." not in login_page.page_source

    yield driver, wait
    driver.close()


@pytest.fixture
def browser_is_opened():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.close()