from playwright.sync_api import Page, expect
from allureWraper import BasePage

class ShoppingCart(BasePage):
    # This class represents the Shopping Cart page in Amazon.
    # It contains locators and methods to validate items in the cart and proceed to checkout.
    def __init__(self, page: Page):
        self.page = page
        # Locator for the Shopping Cart page title
        # This is used to verify that the user has successfully navigated to the cart page
        self.shoppingCartText = page.locator("//h2[contains(text(),'Shopping Cart')]")
        
        # Dynamic locator for a product added to the cart
        # The lambda allows us to pass the item name at runtime
        # Example usage: validaTheVisibilityOfAddedItem("iPhone 16")
        self.addedItem = lambda itemname:page.locator(f"//span[contains(text(),'{itemname}')]")

        # Locator for the "Proceed to Buy" button on the shopping cart page
        # Clicking this button navigates the user to the checkout page
        self.proceedToBuyBtn = page.locator("input[name='proceedToRetailCheckout']")


    def validateTheVisibilityofShoppingCartTitle(self):
        # Validates that the Shopping Cart title is visible.
        # This confirms that the user has successfully navigated to the cart page.
        expect(self.shoppingCartText).to_be_visible()

    def validaTheVisibilityOfAddedItem(self, item):
        # Validates that the specified item is visible in the shopping cart.
        # :param item: Name of the product expected in the cart
        expect(self.addedItem(item).first).to_be_visible()

    def clickOnProceedToBuyBtn(self):
        # Clicks the 'Proceed to Buy' button to navigate to the checkout page.
        self.proceedToBuyBtn.click()