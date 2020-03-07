class SearchResultsPage:
    def __init__(self, driver, wait):
        self.page_source = driver.page_source

    def results_found(self):
        return "We couldn’t find any repositories matching" not in self.page_source
