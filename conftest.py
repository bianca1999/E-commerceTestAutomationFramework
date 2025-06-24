import pytest
from pages.home_page import HomePage
from playwright.sync_api import expect

@pytest.fixture
def go_to_signup_login(page):
    def _go_to_signup_login():
        login_page = HomePage(page)
        login_page.navigate()
        login_page.go_to_signup_login_page()
    return _go_to_signup_login


def delete_account(page):
    def _delete_account():
        page.get_by_role("listitem").filter(has_text="Delete Account").click()
        expect(page).to_have_url("https://automationexercise.com/delete_account")
        expect(page.get_by_text("Account Deleted!")).to_be_visible()
    return _delete_account

