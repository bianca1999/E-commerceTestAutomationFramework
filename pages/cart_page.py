from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page:Page):
        self.page = page
        self.subscription_input = page.locator("//*[@id='susbscribe_email']")
        self.subscribe_button = page.locator('//*[@id="subscribe"]')
        self.success_subscribe_message = page.locator('//*[@id="success-subscribe"]/div')
        self.product_locator = 0
        self.prouct_price = 0
        self.product_quantity = 0
        self.product_total_price = 0

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
        