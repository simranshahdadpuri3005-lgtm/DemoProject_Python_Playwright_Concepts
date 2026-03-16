from playwright.sync_api import Page
import pytest
# Importing the Page class from Playwright.
# Page represents a browser tab where we can perform actions like opening a website,
# clicking buttons, reading text, etc.

@pytest.mark.alert
def test_js_alert(page: Page):
    # This test checks how to handle a simple JavaScript alert popup.

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    # Opens the webpage that contains different JavaScript alert examples.

    # Handle simple alert
    page.once("dialog", lambda dialog: dialog.accept())  #action of handling the alert
    # When an alert dialog appears, this line automatically clicks "OK".
    # "lambda" is a short way to define a small function in one line.

    page.click("text=Click for JS Alert") # Clicks the button on the page which triggers the JavaScript alert popup.

    # Optional verification step
    assert page.locator("#result").inner_text() == "You successfully clicked an alert"
    # After the alert is handled, the page shows a result message.
    # This line checks that the expected success message appears.
    print("Called first time with lambda")
    # Prints a message in the console to confirm this test ran successfully.



# This test is similar to the one above.
# The only difference is that instead of using lambda,
# we define a separate function to handle the alert.

def test_js_alert1(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    def handleAlert(dialog):
        # This function will handle the alert popup by clicking the "OK" button.
        dialog.accept()
    page.once("dialog", handleAlert)  # When the alert appears, Playwright will call the handleAlert function.
    page.locator("text=Click for JS Alert").click() # Clicking this button triggers the alert popup.
    print("called 2nd time with def")  # Console message confirming that the alert was handled using a function.



def test_js_confirm_alert(page: Page):
    # This test handles a JavaScript "Confirm" alert.
    # Confirm alerts have two options: OK and Cancel.
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    # Accept (OK)
    page.once("dialog", lambda dialog: dialog.accept())
    # Automatically clicks "OK" when the confirm alert appears.


    page.click("text=Click for JS Confirm")
    # Clicking this button triggers the confirm alert.

    assert page.locator("#result").inner_text() == "You clicked: Ok"
    # Verifies that the page displays the correct message after clicking OK.
   
    print("clicked ok for second alert")


    
    # Dismiss (Cancel)
    def handle_dismiss(dialog):
        # This function handles the alert by clicking "Cancel".
        dialog.dismiss()

    page.once("dialog", handle_dismiss)
    # Registers the function to handle the next dialog popup.

    page.locator("//button[@onclick='jsConfirm()']").click()
    # Clicking the button again triggers the confirm alert.

    assert page.locator("#result").inner_text() == "You clicked: Cancel"
    # Verifies that the correct message appears after clicking Cancel.

    # We are verifying the text that appears below the "Result" label on the webpage.
    print("clicked cancel for second alert")



def test_js_prompt_alert(page: Page):
    # This test handles a JavaScript Prompt alert.
    # Prompt alerts allow the user to enter some text.

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    # Opens the webpage that contains the prompt alert example.

    page.once(
        "dialog",
        lambda dialog: dialog.accept("Playwright Alert")
    )
    # When the prompt alert appears:
    # - It automatically enters the text "Playwright Alert"
    # - Then it clicks the "OK" button.

    page.click("text=Click for JS Prompt")
    # Clicking this button triggers the prompt alert.

    assert page.locator("#result").inner_text() == "You entered: Playwright Alert"
    # Verifies that the entered text appears correctly in the result section.

    print("text=Click for JS Prompt alert handled successfully")
    # Console message confirming the prompt alert was handled successfully.