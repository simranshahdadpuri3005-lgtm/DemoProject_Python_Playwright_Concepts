from playwright.sync_api import Page, expect
import os


# // Keyboard comands or Keyboard Events Example
def test_keyBoardEvents(page: Page):
    page.goto("https://www.amazon.in/")      # Navigate to Amazon India homepage
    page.locator("input#twotabsearchtextbox").fill("iphone")      # Locate the search textbox and type "iphone"
    

    # (Amazon shows suggestions when text is typed in the search box)
    page.keyboard.press("ArrowDown")     # Press ArrowDown to move through the auto-suggestion list
    page.keyboard.press("Tab")   # Press Tab to move the focus from the suggestion list to the next element
    page.keyboard.press("Enter")      # Press Enter to execute the search
    page.wait_for_timeout(5000) # Wait for 5 seconds to observe the search results page after pressing Enter
    # page.keyboard.press("Escape")      # Press Escape to close popups or suggestion lists if needed


    # Press and Release Keys Separately
    # page.keyboard.down("Control")    # Hold down the Control key
    # # page.keyboard.press("KeyA")   # Example: pressing a key while Control is held
    # page.keyboard.up("Control")    # Release the Control key


    # # Keyboard Shortcuts (Combination Keys)
    # page.keyboard.press("Control+A")   # Select all
    # page.keyboard.press("Control+C")   # Copy
    # page.keyboard.press("Control+V")   # Paste
