from playwright.sync_api import Page

def test_js_alert(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    # Handle simple alert
    page.once("dialog", lambda dialog: dialog.accept())  #action of handling the alert
    page.click("text=Click for JS Alert") # triggering the alert
    # Optional assertion
    assert page.locator("#result").inner_text() == "You successfully clicked an alert"
    print("called first time with lambda")

#this test case is same as above ; just the difference is we are defining the fucntion here and using lambda in above test case

def test_js_alert1(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    def handleAlert(dialog):
        dialog.accept()
    page.once("dialog", handleAlert)  #action of handling the alert
    page.locator("text=Click for JS Alert").click() # triggering the alert
    print("called 2nd time with def")

def test_js_confirm_alert(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    # Accept (OK)
    page.once("dialog", lambda dialog: dialog.accept())
    page.click("text=Click for JS Confirm")
    assert page.locator("#result").inner_text() == "You clicked: Ok"
    print("clicked ok for second alert")
    # Dismiss (Cancel)
    def handle_dismiss(dialog):
        dialog.dismiss()
    page.once("dialog", handle_dismiss)
    page.locator("//button[@onclick='jsConfirm()']").click()
    assert page.locator("#result").inner_text() == "You clicked: Cancel"  
    # we are verifying the tewxt that appears below the result label on the main page
    print("clicked cancel for second alert")



def test_js_prompt_alert(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once(
        "dialog",
        lambda dialog: dialog.accept("Playwright Alert") # accept will enter the text in prompt alert
    )
    page.click("text=Click for JS Prompt")
    assert page.locator("#result").inner_text() == "You entered: Playwright Alert"
    print("text=Click for JS Prompt alert handled successfully")
    