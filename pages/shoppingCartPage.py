from playwright.sync_api import Page, expect
from allureWraper import BasePage

class ShoppingCart(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.shoppingCartText = page.locator("//h2[contains(text(),'Shopping Cart')]")
        self.addedItem = lambda itemname:page.locator(f"//span[contains(text(),'{itemname}')]")
        self.proceedToBuyBtn = page.locator("input[name='proceedToRetailCheckout']")


    def validateTheVisibilityofShoppingCartTitle(self):
        expect(self.shoppingCartText).to_be_visible()

    def validaTheVisibilityOfAddedItem(self, item):
        expect(self.addedItem(item).first).to_be_visible()

    def clickOnProceedToBuyBtn(self):
        self.proceedToBuyBtn.click()