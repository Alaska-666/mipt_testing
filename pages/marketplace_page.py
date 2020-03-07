from selenium.webdriver.support import expected_conditions
from locators.marketplace_page_locators import MarketplacePageLocators


class MarketplacePage():
    def __init__(self, driver, wait):
        self.page_source = driver.page_source
        self.wait = wait
        self.locators = MarketplacePageLocators()

    def activate_logo_link(self):
        element = self.wait.until(expected_conditions.presence_of_element_located(self.locators.LOGO_LINK))
        element.click()