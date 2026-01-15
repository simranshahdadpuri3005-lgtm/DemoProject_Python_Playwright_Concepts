from playwright.sync_api import Page, expect
import allure
from allureWraper import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.emailTextBox = page.locator("#ap_email_login")
        self.submitBtn = page.locator("input[type='submit']")
        self.passwordTextBox = page.locator("#ap_password")

    def enterEmailID(self, emailValue):
        self.emailTextBox.fill(emailValue)

    def clickOnContinueBtn(self):
        self.submitBtn.click()

    def enterPassword(self, passwordValue):
        expect(self.passwordTextBox).to_be_visible()
        self.passwordTextBox.fill(passwordValue)

    

        