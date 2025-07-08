import playwright
import pytest
from playwright.sync_api import Playwright, Page, expect

class SignupPage:
    def __init__(self, page:Page):
        self.page = page

    def set_user_title(self, title):
        if title == 'Mr.':
            self.page.get_by_role("radio", name="Mrs.").check()
            expect(self.page.get_by_role("radio", name="Mrs.")).to_be_checked()
        elif title == 'Mrs':
            self.page.get_by_role("radio", name="Mr.").check()
            expect(self.page.get_by_role("radio", name="Mr.")).to_be_checked()

    def enter_account_information(self,password, birthday, birth_month, birth_year):
        self.page.get_by_label("password").fill(password)
        self.page.locator("#days").select_option(birthday)
        self.page.locator("#months").select_option(birth_month)
        self.page.locator("#years").select_option(birth_year)

    def check_for_newsletter(self):
        self.page.get_by_role("checkbox", name="Sign up for our newsletter!").check()
        expect(self.page.get_by_role("checkbox", name="Sign up for our newsletter!")).to_be_checked()

    def check_for_offers(self):
        self.page.get_by_role("checkbox", name="Receive special offers from").check()
        expect(self.page.get_by_role("checkbox", name="Receive special offers from")).to_be_checked()

    def enter_address_information(self, first_name, last_name, company, address_one, address_two, country, state, city, zipcode, phone):
        self.page.get_by_label("First name ").fill(first_name)
        self.page.get_by_label("Last name ").fill(last_name)
        self.page.locator("#company").fill(company)
        self.page.locator("#address1").fill(address_one)
        self.page.locator("#address2").fill(address_two)
        self.page.get_by_label("Country").select_option(country)
        self.page.get_by_label("State").fill(state)
        self.page.get_by_label("City").fill(city)
        self.page.locator("#zipcode").fill(zipcode)
        self.page.get_by_label("Mobile Number").fill(phone)

        self.page.get_by_role("button", name="Create Account").click()

        expect(self.page).to_have_url("https://automationexercise.com/account_created")
        expect(self.page.get_by_text("Account Created!")).to_be_visible()
         
    def click_continue_button(self):
        self.page.get_by_role("link", name="Continue").click()
        expect(self.page).to_have_url("https://automationexercise.com/")
        expect(self.page.get_by_role("link", name="Logout")).to_be_visible()
        expect(self.page.get_by_text(" Logged in as ")).to_be_visible()
    
    def logout(self):
        self.page.get_by_role("link", name="Logout").click()
        expect(self.page).to_have_url("https://automationexercise.com/login")

        
'''    def delete_account(self):
        self.delete_account_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/delete_account")
        expect(self.page.get_by_text("Account Deleted!")).to_be_visible()
'''        
    
        
