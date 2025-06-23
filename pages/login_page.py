import playwright
import pytest
from playwright.sync_api import Playwright, Page, expect

class LoginPAge:
    def __init__(self, page:Page):
        self.page = page
        self.new_user_name = page.get_by_role("textbox", name="Name")
        self.new_user_email = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.signup_button = page.get_by_role("button", name="Signup")
        self.existing_user_email = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.existing_user_password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def new_user_signup(self, name, email_address):
        self.name.fill(name)
        self.email.fill(email_address)
        self.signup_button.click()

        expect(self.page).to_have_url("https://automationexercise.com/signup")
        expect(self.page.get_by_text("Enter Account Information")).to_be_visible()

    def existing_user_login(self, email, password):
        self.existing_user_email.fill(email)
        self.existing_user_password.fill(password)
        self.login_button.click()


