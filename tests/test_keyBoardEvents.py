from playwright.sync_api import Page, expect
import os


# // Keyboard comands
def test_keyBoardEvents(page: Page):
    page.goto("https://www.amazon.in/")
    page.locator("input#twotabsearchtextbox").fill("iphone")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)
    # page.keyboard.press("Escape")
    # Press and Release Keys Separately
    # page.keyboard.down("Control")
    # # page.keyboard.press("KeyA")
    # page.keyboard.up("Control")

    # # Keyboard Shortcuts (Combination Keys)
    # page.keyboard.press("Control+A")   # Select all
    # page.keyboard.press("Control+C")   # Copy
    # page.keyboard.press("Control+V")   # Paste
