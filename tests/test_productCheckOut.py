from playwright.sync_api import Page, expect
import pytest

@pytest.mark.smoke()
def test_validateProductCheckOut(page:Page, home_page, results_page, shoppingCart_page, logInUsingvalidcreds):
    # home_page.launchTheAmazonBrowser()
    home_page.searchForTheProduct("iphone")
    results_page.clickOnAddToCartBtn("iPhone 16")
    results_page.validateTheVisibilityDecrementIconAfterAddingElementToCart()
    page.wait_for_timeout(3000)
    results_page.clickOnCartBtn()
    shoppingCart_page.validateTheVisibilityofShoppingCartTitle()
    shoppingCart_page.validaTheVisibilityOfAddedItem("iPhone 16")
    shoppingCart_page.clickOnProceedToBuyBtn()
    expect(page).to_have_title("Place Your Order - Amazon Checkout")

@pytest.mark.smoke()
def test_validateTheCheckOutUI(page:Page, home_page, results_page, shoppingCart_page, CheckOut_page, logInUsingvalidcreds):
    # home_page.launchTheAmazonBrowser()
    page.wait_for_timeout(3000)
    page.screenshot(path="screenshots/homepage.png")
    #screenshot command to capture the screenshot of the page
    results_page.clickOnCartBtn()
    shoppingCart_page.clickOnProceedToBuyBtn()
    CheckOut_page.validateTheVisibilityOfdeliverToThisAddressBtn()
    CheckOut_page.validateTheVisibilityOfpaymentMethodText()
    