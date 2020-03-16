from pages.main_page import MainPage
from pages.marketplace_page import MarketplacePage


def test_correct_logo_link(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    current_url = github_main_page.url
    github_main_page.activate_marketplace()
    marketplace_page = MarketplacePage(*browser_is_opened)
    marketplace_page.activate_logo_link()
    assert github_main_page.check_returns_on_main_page(current_url)