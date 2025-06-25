from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.products_button = page.get_by_role("link", name=" Products")
        self.cart_button = page.get_by_role("link", name=" Cart")
        self.signup_login_button = page.get_by_role("link", name=" Signup / Login")
        self.contact_us_button = page.get_by_role("link", name=" Contact us")
        self.test_cases_button = page.get_by_role("link", name=" Test Cases", exact=True)
        self.subscription_input = page.locator("//*[@id='susbscribe_email']")
        self.subscribe_button = page.locator('//*[@id="subscribe"]')
        self.success_subscribe_message = page.locator('//*[@id="success-subscribe"]/div')


    def navigate(self):
        self.page.goto("https://automationexercise.com/")
        expect(self.page).to_have_url("https://automationexercise.com/")

    def go_to_products_page(self):
        self.products_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/products")
        expect(self.page.get_by_text("All Products")).to_be_visible()

    def go_to_cart_page(self):
        self.cart_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/view_cart")


    def go_to_signup_login_page(self):
        self.signup_login_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/login")
        expect(self.page.get_by_role("heading", name="New User Signup!")).to_be_visible()
        expect(self.page.get_by_role("heading", name="Login to your account")).to_be_visible()

    def go_to_test_cases_page(self):
        self.test_cases_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/test_cases")

    def go_to_contact_us_page(self):
        self.contact_us_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/contact_us")
        expect(self.page.get_by_role("heading", name="Get In Touch")).to_be_visible()

    def verify_subscription(self, email_address):
        self.subscription_input.fill(email_address)
        self.subscribe_button.click()
        expect(self.success_subscribe_message).to_be_visible()