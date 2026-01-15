from playwright.sync_api import Page, expect
from allureWraper import BasePage
import allure

# if we do not use the BasePage class here, then the steps will not be recorded in the allure report for this page class

class CheckOutPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.deliverToThisAddressBtn = page.get_by_test_id("secondary-continue-button")
        self.paymentMethodText = page.locator("#checkout-paymentOptionPanel")

    # @allure.step("validating the visibility of deliver to the address")
    # in this way, we can add step in allure report for better readability; just use @allure.step ("requried step def")
    def validateTheVisibilityOfdeliverToThisAddressBtn(self):
        expect(self.deliverToThisAddressBtn).to_be_visible()

    
    # @allure.step("validating the visibility of payment method")
    def validateTheVisibilityOfpaymentMethodText(self):
        expect(self.paymentMethodText).to_be_visible()