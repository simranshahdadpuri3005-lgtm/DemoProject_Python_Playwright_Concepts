from playwright.sync_api import Page, expect
import allure
from allureWraper import BasePage

class LoginPage(BasePage):
    # This class represents the Login Page of Amazon.
    # It contains locators and methods for entering credentials and submitting login forms.
    # Using BasePage ensures all steps are recorded in Allure reports.

    def __init__(self, page: Page):
        # Initializes the page and locators.
        # :param page: Playwright Page object

        self.page = page
        self.emailTextBox = page.locator("#ap_email_login") # Locator for email/username input field
        self.submitBtn = page.locator("input[type='submit']") # Locator for the continue/submit button (used after email or password)
        self.passwordTextBox = page.locator("#ap_password")    # Locator for the password input field

    # Fills the email/username textbox.
    # :param emailValue: Email or username to enter
    @allure.step("Entering Email/Username: {emailValue}")
    def enterEmailID(self, emailValue):
        self.emailTextBox.fill(emailValue)


    # Clicks on the continue/submit button.
    # This is used after entering email or password.
    @allure.step("Clicking on Continue/Submit button")
    def clickOnContinueBtn(self): 
        self.submitBtn.click()

    # Fills the password textbox.
    # Waits for the password field to be visible before entering the value.
    # :param passwordValue: Password to enter

    @allure.step("Entering Password: {passwordValue}")
    def enterPassword(self, passwordValue):
        expect(self.passwordTextBox).to_be_visible()
        self.passwordTextBox.fill(passwordValue)

    

        