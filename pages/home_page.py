from playwright.sync_api import Page, expect
from pages.all_products_page import ProductsPage
from pages.cart_page import CartPage
from pages.contact_us_page import ContactUsPage
from pages.login_page import LoginPage
from pages.test_cases_page import TestCasesPage


class HomePage:
    def __init__(self, page: Page):
        self.page = page


    def navigate(self):
        self.page.goto("https://automationexercise.com/")
        expect(self.page).to_have_url("https://automationexercise.com/")


    def go_to_products_page(self):
        self.page.get_by_role("link", name="Products").click()
        expect(self.page).to_have_url("https://automationexercise.com/products")
        expect(self.page.get_by_text("All Products")).to_be_visible()

        productPage = ProductsPage(self.page)
        return productPage


    def go_to_cart_page(self):
        self.page.get_by_role("link", name="Cart").click()
        expect(self.page).to_have_url("https://automationexercise.com/view_cart")

        cartPage = CartPage(self.page)
        return cartPage


    def go_to_signup_login_page(self):
        self.page.get_by_role("link", name="Signup / Login").click()
        expect(self.page).to_have_url("https://automationexercise.com/login")
        expect(self.page.get_by_role("heading", name="New User Signup!")).to_be_visible()
        expect(self.page.get_by_role("heading", name="Login to your account")).to_be_visible()

        loginPage = LoginPage(self.page)
        return loginPage


    def go_to_test_cases_page(self):
        self.page.get_by_role("link", name=" Test Cases", exact=True).click()
        expect(self.page).to_have_url("https://automationexercise.com/test_cases")

        testcasesPage = TestCasesPage(self.page)
        return testcasesPage


    def go_to_contact_us_page(self):
        self.page.get_by_role("link", name=" Contact us").click()
        expect(self.page).to_have_url("https://automationexercise.com/contact_us")
        expect(self.page.get_by_role("heading", name="Get In Touch")).to_be_visible()

        contactUsPage = ContactUsPage(self.page)
        return contactUsPage


    def verify_subscription(self, email_address):
        self.page.locator("#susbscribe_email").fill(email_address)
        self.page.locator('#subscribe').click()
        expect(self.page.locator('//*[@id="success-subscribe"]/div')).to_be_visible()