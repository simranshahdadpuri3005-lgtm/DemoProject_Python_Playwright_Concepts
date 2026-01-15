
# from playwright.sync_api import expect, Page

# class LoginPage:
    
#     def __init__(self, page: Page):   #page (small p) is fixture and Page (capital P) is class
#         self.page = page
#         self.searchbar= page.locator("input#twotabsearchtextbox")
#         self.account = page.locator("//a[@data-nav-ref='nav_ya_signin']")
#         self.signInBtn = page.locator("#nav-flyout-ya-signin")
#         self.emailId = page.locator("#ap_email_login")
#         self.continueBtn = page.locator(".a-button-input")
#         self.enterPwdValue = page.locator("#ap-password")


#     def launchAmazonPage(self):
#         self.page.goto("https://www.amazon.in/")
#         expect(self.searchbar).to_be_visible()

#     def hoverOnAccountsBtn(self):
#         self.account.hover()

#     def clickOnSignInBtn(self):
#         self.signInBtn.click()

#     def enterEmailID(self, id):
#         self.emailId.fill(id)

#     def clickOnContinueBtn(self):
#         self.continueBtn.click()

#     def enterPassword(self, pwd):
#         self.enterPwdValue.fill(pwd)

