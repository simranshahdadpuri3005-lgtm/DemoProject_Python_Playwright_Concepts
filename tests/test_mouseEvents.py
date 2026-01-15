from playwright.sync_api import Page, expect

def test_mouseEvents(page:Page):
    # page.goto("https://www.amazon.in/")
    # page.hover("//span[contains(text(),'Account & Lists')]")
    # page.mouse.move(300, 200)
    # page.mouse.down()
    # page.mouse.up()
    # Drag and Drop (Using Mouse)
    page.goto("https://practice.expandtesting.com/drag-and-drop?utm_source=chatgpt.com")
    #source = page.locator(page.locator("#column-a"))
    #target = page.locator("#column-b")
    source = "#column-a"
    target = "#column-b"
    page.drag_and_drop(source,target)
    # # Scroll Using Mouse Wheel
    # page.locator("#column-b").scroll_into_view_if_needed()
    page.mouse.wheel(0,400)   # Vertical scroll - first arg is x axis, second is y axis
    page.mouse.wheel(500, 0)   # Horizontal scroll
    # # # Right Click
    # page.locator("#column-a").click(button="right")
    # page.click("#element", button="right")
    # # # Double Click
    # page.dblclick("#element")

    # page.click("#column-a", button="right")
    # page.click("#column-b")

    # page.locator("#column-a").fill("filled")
    # page.fill("#column-b","Dragged")


 