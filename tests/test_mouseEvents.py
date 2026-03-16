from playwright.sync_api import Page, expect

def test_mouseEvents(page:Page):
    # ---------------------------------------------------
    # Example 1: Hover and Basic Mouse Actions (commented)
    # ---------------------------------------------------

    page.goto("https://www.amazon.in/")   # Navigate to Amazon homepage
    page.hover("//span[contains(text(),'Account & Lists')]")  # Hover over the "Account & Lists" menu
    page.mouse.move(300, 200)  # Move mouse pointer to specific screen coordinates (x=300, y=200)
    page.mouse.down() # Press the left mouse button (mouse down)
    page.mouse.up() # Release the left mouse button (mouse up)


    # ---------------------------------------------------
    # Example 2: Drag and Drop Operation using Mouse events
    # ---------------------------------------------------

    # Navigate to drag and drop practice website
    page.goto("https://practice.expandtesting.com/drag-and-drop?utm_source=chatgpt.com")

    # Identify source and target elements for drag and drop
    # Source element: Column A
    # Target element: Column B

    #source = page.locator(page.locator("#column-a"))
    #target = page.locator("#column-b")

    source = "#column-a"
    target = "#column-b"
    page.drag_and_drop(source,target)      # Perform drag and drop from source element to target element



    # ---------------------------------------------------
    # Example 3: Scrolling using Mouse Wheel
    # ---------------------------------------------------

    page.locator("#column-b").scroll_into_view_if_needed()   # Ensures the element is visible in viewport before interacting

    # Scroll vertically down the page
    # mouse.wheel(x, y)
    # x → horizontal scroll
    # y → vertical scroll

    page.mouse.wheel(0,400)   # Vertical scroll - first arg is x axis, second is y axis -  Scroll down 400 pixels vertically
    page.mouse.wheel(500, 0)   # Horizontal scroll to the right -  Scroll right 500 pixels
    
    
    # ---------------------------------------------------
    # Example 5: Right Click (Context Click)
    # ---------------------------------------------------

    # Perform right-click on an element
    page.locator("#column-a").click(button="right")

    # Alternative syntax
   # page.click("#element", button="right")

  # ---------------------------------------------------
    # Example 6: Double Click
    # ---------------------------------------------------

    # Perform double-click on an element
    page.dblclick("#column-a")

 # ---------------------------------------------------
    # Example 7: Additional Click Actions
    # ---------------------------------------------------

    # Right-click on Column A
    page.click("#column-a", button="right")

    # Left-click on Column B
    page.click("#column-b")

     # ---------------------------------------------------
    # Example 8: Filling Text in Elements (commented) -
    # As the elements present are not the input fields, so we cannot fill text in them, 
    # but the below code is an example of how to fill text in input fields using Playwright
    # ---------------------------------------------------

    # Fill text into Column A input element
    #page.locator("#column-a").fill("filled")

    # Fill text into Column B input element
    #page.fill("#column-b", "Dragged")
 