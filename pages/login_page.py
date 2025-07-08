
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page:Page):
        self.page = page

    def user_register(self, name, email_address):
        self.page.get_by_role("textbox", name="Name").fill(name)
        self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(email_address)
        self.page.get_by_role("button", name="Signup").click()

    def expect_register_success(self):
        expect(self.page).to_have_url("https://automationexercise.com/signup")
        expect(self.page.get_by_text("Enter Account Information")).to_be_visible()

    def expect_register_failure(self):
        expect(self.page.get_by_text("Email Address already exist!")).to_be_visible()


    def user_login(self, email, password):
        self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()


    def expect_login_success(self):
        expect(self.page.get_by_text(" Logged in as ")).to_be_visible()

    def expect_login_failure(self):
        expect(self.page.get_by_text("Your email or password is incorrect!")).to_be_visible()






