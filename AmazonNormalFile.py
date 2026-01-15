# from playwright.sync_api import expect, Page

# def launchAmazonPage(page: Page):
#     page.goto("https://www.amazon.in/")
#     searchbar= page.locator("input#twotabsearchtextbox")
#     expect(searchbar).to_be_visible()

# def hoverOnAccountsBtn(page: Page):
#     account = page.locator("//a[@data-nav-ref='nav_ya_signin']")
#     account.hover()

# def clickOnSignInBtn(page: Page):
#     signInBtn = page.locator("#nav-flyout-ya-signin")
#     signInBtn.click()

# def enterEmailID(page: Page, id):
#     emailId = page.locator("#ap_email_login")
#     emailId.fill(id)

# def clickOnContinueBtn(page: Page):
#     continueBtn = page.locator(".a-button-input")
#     continueBtn.click()

# def enterPassword(page: Page, pwd):
#     enterPwdValue = page.locator("#ap-password")
#     enterPwdValue.fill(pwd)

# def test_validLogin(page: Page):
#     launchAmazonPage(page)
#     hoverOnAccountsBtn(page)
#     clickOnSignInBtn(page)
#     enterEmailID(page, 'simran@gmail.com')
#     clickOnContinueBtn(page)
#     enterPassword(page, test14)')
#     clickOnContinueBtn(page)

# def test_invalidLogin(page: Page):
#     launchAmazonPage(page)
#     hoverOnAccountsBtn(page)
#     clickOnSignInBtn(page)
#     enterEmailID(page, 'simran@gmail.com')
#     clickOnContinueBtn(page)
#     enterPassword(page, 'Welcome@')
#     clickOnContinueBtn(page)
    



