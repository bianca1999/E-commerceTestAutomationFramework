from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page:Page):
        self.page = page
        self.subscription_input = page.locator("//*[@id='susbscribe_email']")
        self.subscribe_button = page.locator('//*[@id="subscribe"]')
        self.success_subscribe_message = page.locator('//*[@id="success-subscribe"]/div')
        self.product_locator = 0
        self.product_price = 0
        self.product_quantity = 0
        self.product_total_price = 0
        self.proceed_to_checkout_button = page.get_by_text('Proceed To Checkout')
        self.checkout_form = page.locator('//*[@id="checkoutModal"]/div/div')
        self.register_or_login_button = page.get_by_role("link", name="Register / Login")
        self.address_details = page.get_by_text("Address Details")
        self.review_your_order_section = page.get_by_text("Review Your Order")
        self.message_area = page.locator('//*[@id="ordermsg"]/textarea')
        self.place_order_button = page.get_by_text('Place Order')

    def verify_subscription(self, email_address):
        self.subscription_input.fill(email_address)
        self.subscribe_button.click()
        expect(self.success_subscribe_message).to_be_visible()

    def test_if_a_product_is_in_the_cart(self, product_id, product_price, product_quantity, product_total_price):
        self.product_locator = self.page.locator(f"//*[@id='product-{product_id}']")
        self.product_price = self.page.locator(f"//*[@id='product-{product_id}']/td[3]/p")
        self.product_quantity = self.page.locator(f"//*[@id='product-{product_id}']/td[4]/button")
        self.product_total_price = self.page.locator(f"//*[@id='product-{product_id}']/td[5]/p")
        
        expect(self.product_locator).to_be_visible()
        expect(self.product_price).to_have_text(product_price)
        expect(self.product_quantity).to_have_text(product_quantity)
        expect(self.product_total_price).to_have_text(product_total_price)
    
    def test_total_price_for_a_product(self, product_id, product_total_price):
        self.product_total_price = self.page.locator(f"//*[@id='product-{product_id}']/td[5]/p")
        expect(self.product_total_price).to_have_text(product_total_price)

    def proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()

    def register_or_login_while_checkout(self):
        self.register_or_login_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/login")

    def check_if_address_details_are_visible(self):
        expect(self.address_details).to_be_visible()


    def check_if_review_your_order_section_is_visible(self):
        expect(self.review_your_order_section).to_be_visible()

    def fill_message_area(self, message_text):
        self.message_area.fill(message_text)

    def place_order(self):
        self.place_order_button.click()
        expect(self.page).to_have_url("https://automationexercise.com/payment")

