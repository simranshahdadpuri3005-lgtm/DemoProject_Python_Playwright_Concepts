from playwright.sync_api import Page, expect
from datetime import datetime

# fill in the date by using the below 
# page.locator("input#datepicker").fill("03/01/2026") # format is MM/DD/YYYY


# def test_datePickers(page:Page):
#     page.goto("https://jqueryui.com/datepicker/")
#     # page.frame_locator(".demo-frame").locator("input#datepicker").fill("03/01/2026")
#     # node in dom will start with iframe and hence sometimes th element is not located, if its inside frame
#     frame = page.frame_locator(".demo-frame")
#     frame.locator("input#datepicker").click() #calendear appears
#     frame.locator("a[data-date='14']").click() #click on 14 
#     page.wait_for_timeout(2000)


# This function demonstrates how to select a date using the datepicker
def datePickers(page:Page):
    # Navigate to the jQuery UI datepicker demo page
    page.goto("https://jqueryui.com/datepicker/")
    
    # page.frame_locator(".demo-frame").locator("input#datepicker").fill("02/01/2026") 
    frame = page.frame_locator(".demo-frame") # The datepicker is inside an iframe, so we need to access it via frame_locator
    
    # frame.locator("input#datepicker").fill("02/01/2026")
    frame.locator("input#datepicker").click()  # Click on the input field to open the calendar popup

    # Get the current visible month from the datepicker
    month = frame.locator(".ui-datepicker-month").text_content()
    print(month)
    if(month=='January'):
        frame.locator("//a[@data-date='11']").click()  # If the current month is January, select the 11th



# This function selects a specific month and day (April 11, 2027) in the datepicker
def test_navigate_to_requiredMonth(page: Page): # here the target month is April
    page.goto("https://jqueryui.com/datepicker/")

    frame = page.frame_locator(".demo-frame")
    frame.locator("#datepicker").click() # Click on the input field to open the calendar popup

    target_month = "April"  # Target month to select
    #delare List of entire months
    # List of all months to calculate navigation direction
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # year =[]
    # datetime is a library to get dates
    # current_date = datetime.now() #sytem date
    # current_year = current_date.year 
    # current_month = months[current_date.month - 1]
    
    
    # ---- Step 1: Navigate to the correct year ----
    target_year = 2027
    while True:
        # Get the currently displayed year in the calendar
        current_year = frame.locator(".ui-datepicker-year").text_content()
        current_year = int(current_year)

        # If we are on the target year, stop navigating
        if current_year == target_year:
            break

        # Compare index to decide direction
        # Click prev or next depending on whether we need to go backward or forward
        if current_year > target_year:
            frame.locator(".ui-datepicker-prev").click()
        else:
            frame.locator(".ui-datepicker-next").click()

     # ---- Step 2: Navigate to the correct month ----
    while True:
        # Get the currently displayed month
        current_month = frame.locator(".ui-datepicker-month").text_content() #text_content will give the text of the element

        # If the month matches our target, click the desired date and exit
        if current_month == target_month: #this will be satisfied when current month is april in this case
            frame.locator("//a[text()='11']").click()
            break

        # Compare index to decide direction
        #we are comparing the index of th list of months
        #first case it will 0 for jan and 3 for april
        # then it will be 1 for feb and 3 for april and so on
        #moreover once the above if is satisfid, while loop will break 
        # and we will come out of loop and this next if will not be exeucted

        # Click prev or next depending on whether current month is ahead or behind the target month
        if months.index(current_month) > months.index(target_month):
            frame.locator(".ui-datepicker-prev").click() #click the prev button on calendar
        else:
            frame.locator(".ui-datepicker-next").click()  #click the next button on calendar

    
    # ---- Step 3: Print the selected date from the input field ----
    selected_date = frame.locator("#datepicker").input_value()
    print(f"Selected date is: {selected_date}") # Print selected date from input field