from playwright.sync_api import Page, expect

class ContactUsPage:
    def __init__(self, page:Page):
        self.page = page

    def fill_contact_form(self, name, email, subject, message, input_file=None):
        self.page.get_by_placeholder("Name", exact=True).fill(name)
        self.page.get_by_placeholder("Email", exact=True).fill(email)
        self.page.get_by_placeholder("Subject", exact=True).fill(subject)
        self.page.get_by_placeholder("Your Message Here").fill(message)
        if input_file:
            self.page.locator("input[name='upload_file']").set_input_files(input_file)

        self.page.pause()
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name = "Submit").click()
        #expect(self.submitted_succesfully_message).to_be_visible(timeout=7000)

