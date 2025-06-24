import playwright
import pytest
from playwright.sync_api import Playwright, Page, expect

class SignupPage:
    def __init__(self, page:Page):
        self.page = page
        self.user_title_mrs = page.get_by_role("radio", name="Mrs.")
        self.user_title_mr = page.get_by_role("radio", name="Mr.")

        self.user_name = page.get_by_role("textbox", name="Name *", exact=True)
        self.user_email = page.get_by_role("textbox", name="Email *", exact=True)
        self.user_password = page.get_by_role("textbox", name="Password *")

        self.user_birthday = page.locator("#days")
        self.user_birth_month = page.locator("#months")
        self.user_birth_year = page.locator("#years")

        self.newsletter_checkbox = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.special_offers_checkbox = page.get_by_role("checkbox", name="Receive special offers from")

        self.user_first_name = page.get_by_role("textbox", name="First name *")
        self.user_last_name = page.get_by_role("textbox", name="Last name *")
        self.user_company = page.get_by_role("textbox", name="Company", exact=True)
        self.user_address_one = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.user_address_two = page.get_by_role("textbox", name="Address 2")
        self.user_country = page.get_by_label("Country")
        self.user_state = page.get_by_role("textbox", name="State *")
        self.user_city = page.get_by_role("textbox", name="City *")
        self.user_zipcode = page.locator("#zipcode")
        self.user_phone = page.get_by_role("textbox", name="Mobile Number *")
    
        self.create_account_button = page.get_by_role("button", name="Create Account")
        self.continue_button = page.get_by_role("link", name="Continue")
        self.logout_button = page.get_by_role("link", name=" Logout")
        self.delete_account_button = page.get_by_role("listitem").filter(has_text="Delete Account")

    def set_user_title(self, title):
        if title == 'Mr.':
            self.user_title_mr.check()
            expect(self.user_title_mr).to_be_checked()
        elif title == 'Mrs':
            self.user_title_mrs.check()
            expect(self.user_title_mrs).to_be_checked()

    def enter_account_information(self,password, birthday, birth_month, birth_year):
        self.user_password.fill(password)
        self.user_birthday.select_option(birthday)
        self.user_birth_month.select_option(birth_month)
        self.user_birth_year.select_option(birth_year)

    def check_for_newsletter(self):
        self.newsletter_checkbox.check()
        expect(self.newsletter_checkbox).to_be_checked()

    def check_for_offers(self):
        self.special_offers_checkbox.check()
        expect(self.special_offers_checkbox).to_be_checked()

    def enter_address_information(self, first_name, last_name, company, address_one, address_two, country, state, city, zipcode, phone):
        self.user_first_name.fill(first_name)
        self.user_last_name.fill(last_name)
        self.user_company.fill(company)
        self.user_address_one.fill(address_one)
        self.user_address_two.fill(address_two)
        self.user_country.select_option(country)
        self.user_state.fill(state)
        self.user_city.fill(city)
        self.user_zipcode.fill(zipcode)
        self.user_phone.fill(phone)

        self.create_account_button.click()

        expect(self.page).to_have_url("https://automationexercise.com/account_created")
        expect(self.page.get_by_text("Account Created!")).to_be_visible()
         
    def click_continue_button(self):
        self.continue_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/")
        expect(self.logout_button).to_be_visible()
        expect(self.page.get_by_text(" Logged in as ")).to_be_visible()
    
    def logout(self):
        self.logout_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/login")

        
'''    def delete_account(self):
        self.delete_account_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/delete_account")
        expect(self.page.get_by_text("Account Deleted!")).to_be_visible()
'''        
    
        
