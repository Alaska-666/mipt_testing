from selenium.webdriver.support import expected_conditions
from locators.github_user_page_locators import GitHubUserPageLocators


class GitHubUserPage:
    def __init__(self, driver, wait):
        self.page_source = driver.page_source
        self.driver = driver
        self.title = self.driver.title
        self.wait = wait
        self.locators = GitHubUserPageLocators()

    def create_new_repo(self):
        plus_button = self.wait.until(expected_conditions.presence_of_element_located(self.locators.PLUS_BUTTON))
        plus_button.click()
        elem = self.wait.until(expected_conditions.presence_of_element_located(self.locators.NEW_REPO))
        elem.click()

    def go_in_repo(self):
        elem = self.wait.until(expected_conditions.presence_of_element_located(self.locators.REPO_LINK))
        elem.click()
