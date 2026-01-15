# from AmozonTest_PageObjectModel.pages.amazonLoginPageLocators import LoginPage
# from playwright.sync_api import Page

# def test_validLogin(page: Page):
#     loginPageFunctions = LoginPage(page)   # loginPageFunctions is the object created here
    
#     loginPageFunctions.launchAmazonPage()
#     loginPageFunctions.hoverOnAccount()
#     loginPageFunctions.clickOnSignInBtn()
#     loginPageFunctions.enterEmailID('simran@gmail.com')
#     loginPageFunctions.clickOnContinueBtn()
#     loginPageFunctions.enterPassword('Weltest')
#     loginPageFunctions.clickOnContinueBtn()

# def test_invalidLogin(page: Page):
#     loginPageFunctions = LoginPage(page)   
#     loginPageFunctions.launchAmazonPage()
#     loginPageFunctions.hoverOnAccountsBtn()
#     loginPageFunctions.clickOnSignInBtn()
#     loginPageFunctions.enterEmailID('simran@gmail.com')
#     loginPageFunctions.clickOnContinueBtn()
#     loginPageFunctions.enterPassword('test14')
#     loginPageFunctions.clickOnContinueBtn()