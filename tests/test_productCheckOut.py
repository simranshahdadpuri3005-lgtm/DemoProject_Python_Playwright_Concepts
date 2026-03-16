from playwright.sync_api import Page, expect
import pytest


# -------------------------------------------------------------
# Test Case: Validate Product Checkout Flow
# -------------------------------------------------------------
# This test verifies the end-to-end checkout flow:
# 1. Search for a product
# 2. Add the product to cart
# 3. Validate the product appears in the cart
# 4. Proceed to checkout page


@pytest.mark.smoke()
def test_validateProductCheckOut(page:Page, home_page, results_page, shoppingCart_page, logInUsingvalidcreds):
    # The login fixture (logInUsingvalidcreds) ensures the user is already logged in
    # so we don't need to manually launch the browser or login again.
    
    #home_page.launchTheAmazonBrowser()

    home_page.searchForTheProduct("iphone")     # Search for the product "iphone" from the Amazon home page
    results_page.clickOnAddToCartBtn("iPhone 16")     # On the results page, click "Add to Cart" for the product "iPhone 16"
    results_page.validateTheVisibilityDecrementIconAfterAddingElementToCart()     # Validate that the decrement icon appears
    # (This confirms the product was successfully added to the cart)

    page.wait_for_timeout(3000)      # Static wait to observe UI changes (not recommended for production tests)
    results_page.clickOnCartBtn()     # Click the cart icon to navigate to the shopping cart page
    shoppingCart_page.validateTheVisibilityofShoppingCartTitle()      # Validate the title or heading of the shopping cart page
    shoppingCart_page.validaTheVisibilityOfAddedItem("iPhone 16")     # Verify that the added product "iPhone 16" is visible in the cart
    shoppingCart_page.clickOnProceedToBuyBtn()      # Click the "Proceed to Buy" button to move to the checkout page
    expect(page).to_have_title("Place Your Order - Amazon Checkout")      # Validate that the page title corresponds to the Amazon checkout page


# -------------------------------------------------------------
# Test Case: Validate Checkout Page UI Elements
# -------------------------------------------------------------
# This test verifies the visibility of important UI elements
# on the checkout page such as:
# - Deliver to this address button
# - Payment method section

@pytest.mark.smoke()
def test_validateTheCheckOutUI(page:Page, home_page, results_page, shoppingCart_page, CheckOut_page, logInUsingvalidcreds):
    page.wait_for_timeout(3000)
    page.screenshot(path="screenshots/homepage.png")     # screenshot command to capture the screenshot of the page
    results_page.clickOnCartBtn()
    shoppingCart_page.clickOnProceedToBuyBtn()
    page.screenshot(path="screenshots/shoppingCartPage.png")     # Capture another screenshot of the shopping cart / checkout transition
    
    # Validate that the "Deliver to this address" button is visible
    # This ensures the shipping address section is loaded correctly
    CheckOut_page.validateTheVisibilityOfdeliverToThisAddressBtn()
    # Validate that the payment method section is visible
    # This ensures payment options are displayed correctly
    CheckOut_page.validateTheVisibilityOfpaymentMethodText()
    