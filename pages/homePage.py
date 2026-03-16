import pytest
from playwright.sync_api import Page, expect

class HomePage:
    
    # This class represents the Home Page of Amazon India.
    # It contains all the methods and locators related to actions on the Home Page.
    
    def __init__(self, page:Page):
        self.page = page
        self.accntBtn  = page.locator("#nav-link-accountList") # Locator for the Account & Lists button (top-right navigation)
       # self.signInBtn = page.locator(".nav-action-inner")
        
        self.signInBtn = page.get_by_role("link", name="Sign in") # Locator for the Sign In link under Account & Lists
        
        self.searchTab = page.locator("input#twotabsearchtextbox") # Locator for the search input textbox
        self.searchBtn = page.locator("input#nav-search-submit-button") # Locator for the search button
        self.switchAccountBtn = page.locator("#nav-item-switch-account") # Locator for the "Switch Account" button (appears if multiple accounts exist)
        

    # Clicks on the Account & Lists button.
    # Originally designed to hover, but click works for opening the dropdown menu.
    def hoverOnAccountsBtn(self):
        self.accntBtn.click()

    # Clicks on the Sign In link under the Account & Lists dropdown.
    # Optionally, can assert visibility before clicking.
    def clickOnSignInBtn(self):
        #expect(self.signInBtn).to_be_visible()
        self.signInBtn.click()

    # Opens the Amazon India homepage.
    # Waits for the Account button to ensure page has loaded.
    # Adds an extra wait to allow all dynamic elements to load
    def launchTheAmazonBrowser(self):
        self.page.goto("https://www.amazon.in/")
        self.accntBtn.wait_for(timeout=40000) # Wait up to 40 seconds for the Account button
        self.page.wait_for_timeout(5000)        # Extra 5 seconds pause for page stability


    #  Searches for a product using the search bar.
    #  Fills the input and clicks the search button.
    #  :param value: Name of the product to search for

    def searchForTheProduct(self, value):
        self.searchTab.fill(value)
        self.searchBtn.click()

    # Validates that the 'Switch Account' button is present on the page.
    # Useful after login to verify multiple accounts.

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
    
        