from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.join_gihub_page import JoinGithubPage
from pages.marketplace_page import MarketplacePage
import random


def test_gihub_search(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    github_main_page.search("github")
    search_results_page = SearchResultsPage(*browser_is_opened)
    assert search_results_page.results_found()


def test_incorrect_username_input(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    id_check_input = github_main_page.username("__strange__name*").get_attribute("aria-describedby")
    assert not github_main_page.check_input_field(id_check_input,
                                                  "Username may only contain alphanumeric characters or single hyphens,"
                                                  " and cannot begin or end with a hyphen.")


def test_not_available_username_input(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    username_input = "alaska-666"
    id_check_input = github_main_page.username(username_input).get_attribute("aria-describedby")
    assert not github_main_page.check_input_field(id_check_input, f"Username {username_input} is not available")


def test_incorrect_email_input(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    id_check_input = github_main_page.email("email").get_attribute("aria-describedby")
    assert not github_main_page.check_input_field(id_check_input, "Email is invalid or already taken")


def test_taken_email(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    id_check_input = github_main_page.email("pangolin-666@mail.ru").get_attribute("aria-describedby")
    assert not github_main_page.check_input_field(id_check_input, "Email is invalid or already taken")


def test_incorrect_password(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    github_main_page.password("12345678910")
    join_github_page = JoinGithubPage(*browser_is_opened)
    assert join_github_page.message_found("Password is weak and can be easily guessed")


def test_create_account(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    username = "new-user" + str(random.randint(1, 100))*random.randint(1, 10)
    id_check_input = github_main_page.username(username).get_attribute("aria-describedby")
    assert (github_main_page.check_input_field(id_check_input, f"Username {username} is not available") and
            github_main_page.check_input_field(id_check_input,
                                               "Username may only contain alphanumeric characters or single hyphens,"
                                               " and cannot begin or end with a hyphen."))
    email = "my-good-mail" + str(random.randint(1, 10))*random.randint(1, 10) + "@mail.ru"
    id_check_input = github_main_page.email(email).get_attribute("aria-describedby")
    print(email)
    assert github_main_page.check_input_field(id_check_input, "Email is invalid or already taken")
    github_main_page.password("veryGoodPassword1937284509735427")
    join_github_page = JoinGithubPage(*browser_is_opened)
    assert (not join_github_page.message_found("There were problems creating your account.") and
            join_github_page.message_found("Verify your account"))


def test_correct_logo_link(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    current_url = github_main_page.url
    github_main_page.activate_marketplace()
    marketplace_page = MarketplacePage(*browser_is_opened)
    marketplace_page.activate_logo_link()
    assert github_main_page.check_returns_on_main_page(current_url)