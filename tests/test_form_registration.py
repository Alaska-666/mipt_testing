from pages.join_gihub_page import JoinGithubPage
from users.user_generator import UserGenerator
from users.user import User
from pages.main_page import MainPage


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
