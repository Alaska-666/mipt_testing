from selenium.webdriver.common.by import By


class MainPageLocators:
    def __init__(self):
        self.SEARCH_INPUT = (By.NAME, "q")
        self.USERNAME = (By.ID, "user[login]-footer")
        self.EMAIL = (By.ID, "user[email]-footer")
        self.PASSWORD = (By.ID, "user[password]-footer")
        self.MARKETPLACE_LINK = (By.CSS_SELECTOR, "body > div.position-relative.js-header-wrapper > header > div > div."
                                                  "HeaderMenu.HeaderMenu--logged-out.position-fixed.top-0.right-0."
                                                  "bottom-0.height-fit.position-lg-relative.d-lg-flex.flex-justify-"
                                                  "between.flex-items-center.flex-auto > nav > ul > li:nth-child(4) > a")
