import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser_is_opened():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.close()