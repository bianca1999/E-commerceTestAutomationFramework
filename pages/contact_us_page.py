from playwright.sync_api import Page, expect

class ContactUsPage:
    def __init__(self, page:Page):
        self.page = page
        self.name =  page.locator("input[data-qa='name']")
        self.email = page.locator("input[data-qa='email']")
        self.subject = page.locator("input[data-qa='subject']")
        self.message = page.locator("textarea[data-qa='message']")
        self.upload_file_button = page.locator("input[name='upload_file']")
        self.submit_button = page.locator("input[data-qa='submit-button']")
        self.submitted_succesfully_message = page.locator("div.status.alert.alert-success")


    def fill_contact_form(self, name, email, subject, message, input_file=None):
        self.name.fill(name)
        self.email.fill(email)
        self.subject.fill(subject)
        self.message.fill(message)
        if input_file:
            self.upload_file_button.set_input_files(input_file)

        self.page.pause()
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_button.click()
        #expect(self.submitted_succesfully_message).to_be_visible(timeout=7000)

