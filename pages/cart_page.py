from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page:Page):
        self.subscription_input = page.locator("//*[@id='susbscribe_email']")
        self.subscribe_button = page.locator('//*[@id="subscribe"]')
        self.success_subscribe_message = page.locator('//*[@id="success-subscribe"]/div')

    def verify_subscription(self, email_address):
        self.subscription_input.fill(email_address)
        self.subscribe_button.click()
        expect(self.success_subscribe_message).to_be_visible()

