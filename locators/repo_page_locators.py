from selenium.webdriver.common.by import By


class RepoPageLocators:
    def __init__(self):
        self.CLONE_BUTTON = (By.CSS_SELECTOR, "#js-repo-pjax-container > div.container-lg.clearfix.new-discussion-"
                                              "timeline.px-3 > div > div.file-navigation.in-mid-page.d-flex.flex-items-"
                                              "start > span > details > summary")
        self.COPY_HTML_BUTTON = (By.CSS_SELECTOR, "#js-repo-pjax-container > div.container-lg.clearfix.new-discussion-"
                                                  "timeline.px-3 > div > div.file-navigation.in-mid-page.d-flex.flex-"
                                                  "items-start > span > details > div > div > div.get-repo-modal-"
                                                  "options > div.clone-options.https-clone-options > div > div > "
                                                  "clipboard-copy")
