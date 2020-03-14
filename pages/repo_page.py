from locators.repo_page_locators import RepoPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class RepoPage:
    def __init__(self, driver, wait):
        self.page_source = driver.page_source
        self.driver = driver
        self.title = self.driver.title
        self.wait = wait
        self.locators = RepoPageLocators()

    def check_clone_probability(self):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.CLONE_BUTTON))
        element.click()
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.locators.COPY_HTML_BUTTON))
            return True
        except TimeoutException:
            return False
