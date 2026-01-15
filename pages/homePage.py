import pytest
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.accntBtn  = page.locator("#nav-link-accountList")
       # self.signInBtn = page.locator(".nav-action-inner")
        
        self.signInBtn = page.get_by_role("link", name="Sign in")
        
        self.searchTab = page.locator("input#twotabsearchtextbox")
        self.searchBtn = page.locator("input#nav-search-submit-button")
        self.switchAccountBtn = page.locator("#nav-item-switch-account")
        
    
    def hoverOnAccountsBtn(self):
        self.accntBtn.click()

    def clickOnSignInBtn(self):
        #expect(self.signInBtn).to_be_visible()
        self.signInBtn.click()

    def launchTheAmazonBrowser(self):
        self.page.goto("https://www.amazon.in/")
        self.accntBtn.wait_for(timeout=40000)
        self.page.wait_for_timeout(5000)

    def searchForTheProduct(self, value):
        self.searchTab.fill(value)
        self.searchBtn.click()

    def validateTheVisibilityOfSwitchAccount(self):
        expect(self.switchAccountBtn).to_have_count(1)
    
    # def hoverOnAccountsBtn(self):
    #     self.account.hover()

    # def clickOnSignInBtn(self):
    #     self.account.wait_for()
    #     self.signInBtn.click()


    # def launchTheAmazonBrowser(self):
    #     self.page.goto("https://www.amazon.in/")
    #     self.account.wait_for(timeout=40000)

    # def searchForProduct(self, value):
    #     self.searchTab.fill(value)
    #     self.searchBtn.click()
    
        