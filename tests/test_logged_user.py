from pages.github_user_page import GitHubUserPage
from pages.create_new_repo_page import CreateNewRepoPage
from pages.repo_page import RepoPage
from pages.login_page import LoginPage
from users.user_generator import UserGenerator


def test_sign_in(user_is_logged_in):
    github_user_page = GitHubUserPage(*user_is_logged_in)
    assert "GitHub" in github_user_page.title
    assert "Learn Git and GitHub without any code!" in github_user_page.page_source


def test_create_new_repo(user_is_logged_in):
    github_user_page = GitHubUserPage(*user_is_logged_in)
    assert "GitHub" in github_user_page.title

    github_user_page.create_new_repo()
    create_new_repo_page = CreateNewRepoPage(*user_is_logged_in)
    assert "Create a new repository" in create_new_repo_page.page_source


def test_clone_repo(user_is_logged_in):
    github_user_page = GitHubUserPage(*user_is_logged_in)
    assert "GitHub" in github_user_page.title

    github_user_page.go_in_repo()
    repo_page = RepoPage(*user_is_logged_in)
    assert repo_page.check_clone_probability()
