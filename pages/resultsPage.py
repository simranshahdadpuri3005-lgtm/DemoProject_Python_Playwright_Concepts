from playwright.sync_api import Page, expect
from allureWraper import BasePage

productDataPath = "testData/shoppingCartDetails.json"  # Path to JSON file that stores shopping cart related test data

class ResultsPage():
    # This class represents the Search Results Page in Amazon.
    # It contains locators and actions related to products displayed after performing a search.

    def __init__(self, page: Page):
        self.page = page
        self.resultsText = page.locator("//div[@data-cy ='title-recipe']//h2")         # Locator for product titles displayed in the search results
        
        # Dynamic locator for the "Add to Cart" button for a specific product.
        # The lambda allows passing the product name at runtime.
        # Example usage: clickOnAddToCartBtn("iPhone 16")
        self.addToCartBtn = lambda product_name:page.locator(f"//span[contains(text(),'{product_name}')]//ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@name='submit.addToCart']")
        
        # Locator for the decrement icon (appears after a product is added to the cart)
        # Used to reduce the quantity of the product in the cart
        self.decrementicon = page.locator("span[data-a-selector='decrement-icon']")
        
        
        self.cartIcon = page.locator("#nav-cart-text-container")        # Locator for the shopping cart icon in the Amazon navigation bar

        #self.resultsText = page.locator("span.a-color-state.a-text-bold")         # Alternative locator for results text (kept for reference)
        # by providing f function and a variable inside the locator we can use the string

    def getResultsText(self):
        # Returns the text content of the search results header.
        # Useful for validating that the correct search results page is displayed.
        return self.resultsText.text_content()
    
    def clickOnAddToCartBtn(self, product):
        # Clicks on the 'Add to Cart' button for the specified product.
        # :param product: Name of the product to add to the cart
        self.addToCartBtn(product).first.click()

    
    def validateTheVisibilityDecrementIconAfterAddingElementToCart(self):
        # Validates that the decrement icon is visible after adding
        # a product to the cart. This confirms that the item was added successfully.
        expect(self.decrementicon.first).to_be_visible()

    def clickOnDecrementIcon(self):
        # Clicks the decrement icon to reduce the quantity of the product in the shopping cart.
        self.decrementicon.first.click()
    
    def validateThatDecrementIconIsNotVisible(self):
        # Validates that the decrement icon is no longer visible, indicating that the item quantity has been reduced to zero
        # or removed from the cart.
        expect(self.decrementicon.first).not_to_be_visible()

    def clickOnCartBtn(self):
        #Clicks the cart icon to navigate to the shopping cart page.
        self.cartIcon.click()