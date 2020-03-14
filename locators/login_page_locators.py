from selenium.webdriver.common.by import By


class LoginPageLocators:
    def __init__(self):
        self.LOGIN_INPUT = (By.ID, "login_field")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.SIGN_IN_BUTTON = (By.NAME, "commit")