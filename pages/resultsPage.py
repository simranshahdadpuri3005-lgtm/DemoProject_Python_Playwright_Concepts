from playwright.sync_api import Page, expect
from allureWraper import BasePage

productDataPath = "testData/shoppingCartDetails.json"

class ResultsPage():
    def __init__(self, page: Page):
        self.page = page
        self.resultsText = page.locator("//div[@data-cy ='title-recipe']//h2")
        self.addToCartBtn = lambda product_name:page.locator(f"//span[contains(text(),'{product_name}')]//ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@name='submit.addToCart']")
        self.decrementicon = page.locator("span[data-a-selector='decrement-icon']")
        self.cartIcon = page.locator("#nav-cart-text-container")

        #self.resultsText = page.locator("span.a-color-state.a-text-bold")
        #by providing f function and a variable inside the locator we can use the string

    def getResultsText(self):
        return self.resultsText.text_content()
    
    def clickOnAddToCartBtn(self, product):
        self.addToCartBtn(product).first.click()

    
    def validateTheVisibilityDecrementIconAfterAddingElementToCart(self):
        expect(self.decrementicon.first).to_be_visible()

    def clickOnDecrementIcon(self):
        self.decrementicon.first.click()
    
    def validateThatDecrementIconIsNotVisible(self):
        expect(self.decrementicon.first).not_to_be_visible()

    def clickOnCartBtn(self):
        self.cartIcon.click()