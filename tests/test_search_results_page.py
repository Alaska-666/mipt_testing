from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


def test_gihub_search(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    github_main_page.search("github")
    search_results_page = SearchResultsPage(*browser_is_opened)
    assert search_results_page.results_found()
