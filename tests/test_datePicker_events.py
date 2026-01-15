from playwright.sync_api import Page, expect
from datetime import datetime


# page.locator("input#datepicker").fill("03/01/2026")

def test_datePickers(page:Page):
    page.goto("https://jqueryui.com/datepicker/")
    # page.frame_locator(".demo-frame").locator("input#datepicker").fill("03/01/2026")
    frame = page.frame_locator(".demo-frame")
    frame.locator("input#datepicker").click()
    frame.locator("a[data-date='14']").click()
    page.wait_for_timeout(2000)



def datePickers(page:Page):
    page.goto("https://jqueryui.com/datepicker/")
    # page.frame_locator(".demo-frame").locator("input#datepicker").fill("02/01/2026")
    frame = page.frame_locator(".demo-frame")
    # frame.locator("input#datepicker").fill("02/01/2026")
    frame.locator("input#datepicker").click()
    month = frame.locator(".ui-datepicker-month").text_content()
    print(month)
    if(month=='January'):
        frame.locator("//a[@data-date='11']").click()


def navigate_to_january(page: Page):
    page.goto("https://jqueryui.com/datepicker/")

    frame = page.frame_locator(".demo-frame")
    frame.locator("#datepicker").click()

    target_month = "April"
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # year =[]

    # current_date = datetime.now()
    # current_year = current_date.year
    # current_month = months[current_date.month - 1]

    target_year = 2027
    while True:
        current_year = frame.locator(".ui-datepicker-year").text_content()

        if current_year == target_year:
            break

        # Compare index to decide direction
        if current_year > months.index(target_month):
            frame.locator(".ui-datepicker-prev").click()
        else:
            frame.locator(".ui-datepicker-next").click()

    
    while True:
        current_month = frame.locator(".ui-datepicker-month").text_content()

        if current_month == target_month:
            frame.locator("//a[text()='11']").click()
            break

        # Compare index to decide direction
        if months.index(current_month) > months.index(target_month):
            frame.locator(".ui-datepicker-prev").click()
        else:
            frame.locator(".ui-datepicker-next").click()

    