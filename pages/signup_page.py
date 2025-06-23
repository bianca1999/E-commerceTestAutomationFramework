import playwright
import pytest
from playwright.sync_api import Playwright, Page, expect

class SignupPage:
    def __init__(self, page:Page):
        self.page = page
        self.user_title_mrs = page.get_by_role("radio", name="Mrs.")
        self.user_title_mr = page.get_by_role("radio", name="Mr.")

        self.user_name = page.get_by_role("textbox", name="Name *")
        self.user_email = page.get_by_role("textbox", name="Email *")
        self.user_password = page.get_by_role("textbox", name="Password *")

        self.user_birthday = page.locator("#days")
        self.user_birth_month = page.locator("#months")
        self.user_birth_yeatr = page.locator("#years")

        self.newsletter_checkbox = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.special_offers_checkbox = page.get_by_role("checkbox", name="Receive special offers from")

        self.user_first_name = page.get_by_role("textbox", name="First name *")
        self.user_last_name = page.get_by_role("textbox", name="Last name *")
        self.user_company = page.get_by_role("textbox", name="Company", exact=True)
        self.user_address_one = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.user_address_two = page.get_by_role("textbox", name="Address 2").click()
        self.user_country = page.get_by_label("Country")
        self.user_state = page.get_by_role("textbox", name="State *")
        self.user_city = page.page.get_by_role("textbox", name="City * Zipcode *")
        self.user_zipcode = page.locator("#zipcode")
        self.user_phone = page.get_by_role("textbox", name="Mobile Number *")
    
        self.create_account_button = page.get_by_role("button", name="Create Account")


    