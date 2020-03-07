class JoinGithubPage:
    def __init__(self, driver, wait):
        self.page_source = driver.page_source

    def message_found(self, message):
        return message in self.page_source