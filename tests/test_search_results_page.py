from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.join_gihub_page import JoinGithubPage
from pages.marketplace_page import MarketplacePage
from pages.create_new_repo_page import CreateNewRepoPage
from pages.repo_page import RepoPage
from pages.login_page import LoginPage
from pages.github_user_page import GitHubUserPage
from users.user_generator import UserGenerator
from users.user import User


def test_gihub_search(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    github_main_page.search("github")
    search_results_page = SearchResultsPage(*browser_is_opened)
    assert search_results_page.results_found()


def test_incorrect_username_input(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    id_check_input = github_main_page.username(User(username="__strange__name*")).get_attribute("aria-describedby")
    assert not github_main_page.check_input_field(id_check_input,
                                                  "Username may only contain alphanumeric characters or single hyphens,"
                                                  " and cannot begin or end with a hyphen.")


def test_not_available_username_input(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    user = User(username="alaska-666")
    id_check_input = github_main_page.username(user).get_attribute("aria-describedby")
    assert not github_main_page.check_input_field(id_check_input, f"Username {user.username} is not available")


def test_incorrect_email_input(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    id_check_input = github_main_page.email(User(email="email")).get_attribute("aria-describedby")
    assert not github_main_page.check_input_field(id_check_input, "Email is invalid or already taken")


def test_taken_email(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    id_check_input = github_main_page.email(User(email="pangolin-666@mail.ru")).get_attribute("aria-describedby")
    assert not github_main_page.check_input_field(id_check_input, "Email is invalid or already taken")


def test_incorrect_password(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title
    github_main_page.password(User(password="12345678910"))
    join_github_page = JoinGithubPage(*browser_is_opened)
    assert join_github_page.message_found("Password is weak and can be easily guessed")


def test_create_account(browser_is_opened):
    github_main_page = MainPage(*browser_is_opened)
    assert "GitHub" in github_main_page.title

    github_main_page.full_registration(UserGenerator.generate_random_user())

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


def test_sign_in(browser_is_opened):
    login_page = LoginPage(*browser_is_opened)
    assert "Sign in to GitHub" in login_page.title

    login_page.full_authorization(UserGenerator.generate_from_json("users/testuser.json"))
    assert "Incorrect username or password." not in login_page.page_source

    github_user_page = GitHubUserPage(*browser_is_opened)
    assert "GitHub" in github_user_page.title
    assert "Learn Git and GitHub without any code!" in github_user_page.page_source


def test_create_new_repo(browser_is_opened):
    login_page = LoginPage(*browser_is_opened)
    assert "Sign in to GitHub" in login_page.title

    login_page.full_authorization(UserGenerator.generate_from_json("users/testuser.json"))
    assert "Incorrect username or password." not in login_page.page_source

    github_user_page = GitHubUserPage(*browser_is_opened)
    assert "GitHub" in github_user_page.title

    github_user_page.create_new_repo()
    create_new_repo_page = CreateNewRepoPage(*browser_is_opened)
    assert "Create a new repository" in create_new_repo_page.page_source


def test_clone_repo(browser_is_opened):
    login_page = LoginPage(*browser_is_opened)
    assert "Sign in to GitHub" in login_page.title

    login_page.full_authorization(UserGenerator.generate_from_json("users/testuser.json"))
    assert "Incorrect username or password." not in login_page.page_source

    github_user_page = GitHubUserPage(*browser_is_opened)
    assert "GitHub" in github_user_page.title

    github_user_page.go_in_repo()
    repo_page = RepoPage(*browser_is_opened)
    assert repo_page.check_clone_probability()
