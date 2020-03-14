from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions
from users.user import User


URL = "https://github.com/login"


class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.driver.get(URL)
        self.wait = wait
        self.locators = LoginPageLocators()
        self.title = self.driver.title
        self.page_source = driver.page_source

    def login(self, user: User):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.LOGIN_INPUT))
        element.clear()
        element.send_keys(user.username)

    def password(self, user: User):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.PASSWORD_INPUT))
        element.clear()
        element.send_keys(user.password)

    def sign_in_buttion_activate(self):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.SIGN_IN_BUTTON))
        element.click()

    def full_authorization(self, user: User):
        self.login(user)
        self.password(user)
        self.sign_in_buttion_activate()
