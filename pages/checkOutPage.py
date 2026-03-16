from playwright.sync_api import Page, expect
from allureWraper import BasePage
import allure

# if we do not use the BasePage class here, then the steps will not be recorded in the allure report for this page class

# The CheckOutPage class represents the Checkout page in Amazon's UI.
# Extending BasePage ensures that Allure steps are recorded automatically for better reporting.
class CheckOutPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        # Locator for the "Deliver to this address" button
        self.deliverToThisAddressBtn = page.get_by_test_id("secondary-continue-button")
        # Locator for the payment method panel section
        self.paymentMethodText = page.locator("#checkout-paymentOptionPanel")

    # @allure.step("validating the visibility of deliver to the address")
    # in this way, we can add step in allure report for better readability; just use @allure.step ("requried step def")


    # This method validates that the "Deliver to this address" button is visible on the page
    # Using @allure.step decorator here would add this as a step in the Allure report
    # Example: @allure.step("Validate visibility of 'Deliver to this address' button")
    def validateTheVisibilityOfdeliverToThisAddressBtn(self):
        expect(self.deliverToThisAddressBtn).to_be_visible() # Assertion: button must be visible

    
    @allure.step("validating the visibility of payment method")
    # This method validates that the payment method panel is visible on the checkout page
    # Example of adding Allure step: @allure.step("Validate visibility of payment method panel")
    def validateTheVisibilityOfpaymentMethodText(self):
        expect(self.paymentMethodText).to_be_visible() # Assertion: payment method section must be visible