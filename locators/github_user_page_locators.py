from selenium.webdriver.common.by import By


class GitHubUserPageLocators:
    def __init__(self):
        self.PLUS_BUTTON = (By.CSS_SELECTOR, "body > div.position-relative.js-header-wrapper > header > "
                                             "div:nth-child(6) > details > summary")
        self.NEW_REPO = (By.CSS_SELECTOR, "body > div.position-relative.js-header-wrapper > header > "
                                          "div:nth-child(6) > details > details-menu > a:nth-child(1)")
        self.REPO_LINK = (By.CSS_SELECTOR, "body > div.application-main > div > aside.team-left-column.col-12.col-md-4."
                                           "col-lg-3.bg-white.border-right.border-bottom.hide-md.hide-sm > div."
                                           "dashboard-sidebar.js-sticky.top-0.px-3.px-md-4.px-lg-4.overflow-auto > "
                                           "div.mb-3.Details.js-repos-container.mt-5 > div > ul > li > div > a > div")
