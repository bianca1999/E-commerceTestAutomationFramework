from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


class CartPage:
    def __init__(self, page:Page):
        self.page = page

    def verify_subscription(self, email_address):
        self.page.locator("#susbscribe_email").fill(email_address)
        self.page.locator('#subscribe').click()
        expect(self.page.locator('#success-subscribe')).to_be_visible()

    def test_if_a_product_is_in_the_cart(self, product_id, product_price, product_quantity, product_total_price):
        expect(self.page.locator(f"#product-{product_id}")).to_be_visible()
        expect(self.page.locator(f"#product-{product_id} .cart_price")).to_have_text(product_price)
        expect(self.page.locator(f"#product-{product_id} .cart_quantity")).to_have_text(product_quantity)
        expect(self.page.locator(f"#product-{product_id} .cart_total")).to_have_text(product_total_price)
    
    def test_total_price_for_a_product(self, product_id, product_total_price):
        expect(self.page.locator(f"//*[@id='product-{product_id}']/td[5]/p")).to_have_text(product_total_price)

    def proceed_to_checkout(self):
        self.page.get_by_text('Proceed To Checkout').click()

    def register_or_login_while_checkout(self):
        self.page.get_by_role("link", name="Register / Login").click()
        expect(self.page).to_have_url("https://automationexercise.com/login")

        loginPage = LoginPage(self.page)
        return loginPage

    def check_if_address_details_are_visible(self):
        expect(self.page.get_by_text("Address Details")).to_be_visible()

    def check_if_review_your_order_section_is_visible(self):
        expect(self.page.get_by_text("Review Your Order")).to_be_visible()

    def fill_message_area(self, message_text):
        self.page.locator('textarea').fill(message_text)

    def place_order(self):
        self.page.get_by_role("link", name='Place Order').click()
        expect(self.page).to_have_url("https://automationexercise.com/payment")

    def remove_a_product_from_the_cart(self, product_id):
        self.page.locator(f"#product-{product_id} .cart_quantity_delete").click()
        expect(self.page.locator(f"#product-{product_id}")).not_to_be_visible()
