import playwright
import pytest
from playwright.sync_api import Playwright, Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page


    def navigate(self):
        self.page.goto("https://automationexercise.com/")
        expect(self.page).to_have_url("https://automationexercise.com/")

    def go_to_products_page(self):
        self.page.get_by_role("link", name=" Products").click()
        expect(self.page).to_have_url("https://automationexercise.com/products")

    def go_to_cart_page(self):
        self.page.get_by_role("link", name=" Cart").click()
        expect(self.page).to_have_url("https://automationexercise.com/view_cart")


    def go_to_signup_login_page(self):
        self.page.get_by_role("link", name=" Signup / Login").click()
        expect(self.page).to_have_url("https://automationexercise.com/login")
        expect(self.page.get_by_role("heading", name="New User Signup!")).to_be_visible()
