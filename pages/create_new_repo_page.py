class CreateNewRepoPage:
    def __init__(self, driver, wait):
        self.page_source = driver.page_source
        self.driver = driver
        self.title = self.driver.title
