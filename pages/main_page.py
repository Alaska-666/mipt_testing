from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


URL = "https://github.com/"


class MainPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.locators = MainPageLocators()
        self.driver.get(URL)
        self.title = self.driver.title
        self.url = driver.current_url

    def search(self, search_string: str):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.SEARCH_INPUT))
        element.clear()
        element.send_keys(search_string)
        element.send_keys(Keys.RETURN)

    def username(self, input_string: str):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.USERNAME))
        element.clear()
        element.send_keys(input_string)
        return element

    def check_input_field(self, id_check_input, checking_string):
        try:
            element = self.wait.until(expected_conditions.presence_of_element_located((By.ID, id_check_input)))
            source = element.get_attribute("outerHTML")
        except TimeoutException:
            return True
        return checking_string not in source

    def email(self, input_string: str):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.EMAIL))
        element.clear()
        element.send_keys(input_string)
        return element

    def password(self, input_string: str):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.PASSWORD))
        element.clear()
        element.send_keys(input_string)
        element.send_keys(Keys.RETURN)

    def sign_up_button_activate(self):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.SIGN_UP_BUTTON))
        element.click()

    def activate_marketplace(self):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.MARKETPLACE_LINK))
        element.click()

    def check_returns_on_main_page(self, url):
        return url == self.driver.current_url
