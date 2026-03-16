import pytest
from playwright.sync_api import sync_playwright
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from pages.resultsPage import ResultsPage
from pages.shoppingCartPage import ShoppingCart
from pages.checkOutPage import CheckOutPage

# we are overriding the page to see the execution clearly by explicitly providing the steps
# we are just redeclare the page fixture and how it should behave

# if the scope is session, then the browser will be launched only once for the entire test suite
# if the scope is function, then the browser will be launched for every test case

@pytest.fixture(scope="function")
def page():    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=5000)
        page = browser.new_page()
        yield page
        browser.close()


#creation of objects in conftest will help in reducing the object creation again and again for test cases
@pytest.fixture()
def home_page(page):
    home_page = HomePage(page)
    #after creation of this object, constructor will automatically triggered
    return home_page

@pytest.fixture()
def login_page(page):
    login_page = LoginPage(page)
    return login_page

@pytest.fixture()
def results_page(page):
    results_page = ResultsPage(page)
    return results_page

@pytest.fixture()
def shoppingCart_page(page):
    shoppingCart_page = ShoppingCart(page)
    return shoppingCart_page

@pytest.fixture()
def CheckOut_page(page):
    CheckOut_page = CheckOutPage(page)
    return CheckOut_page

# we are creating a fixture for login using valid credentials
# then we can comment the same test case in login page and use this fixture as a pre requisite for other test cases

@pytest.fixture(scope="function")
def logInUsingvalidcreds(page, home_page, login_page):
    home_page.launchTheAmazonBrowser()
    #home_page.hoverOnAccountsBtn()
    home_page.clickOnSignInBtn()
    login_page.enterEmailID("trainingplaywright@gmail.com")
    login_page.clickOnContinueBtn()
    login_page.enterPassword("Welcome@04")
    login_page.clickOnContinueBtn()
    yield
   # print("Log out code can be added here")


import pytest
import allure


# using this hook implementation, we can capture the screenshot on test failure
# hooks are similar to event listeners; they listen to the events happening during the test execution

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()

#     if report.when == "call" and report.failed:
#         page = item.funcargs.get("page", None)
#         if page:
#             screenshot = page.screenshot()
#             allure.attach(
#                 screenshot,
#                 name="Failure Screenshot",
#                 attachment_type=allure.attachment_type.PNG
#             )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshots for setup, call, and teardown failures
    if report.failed:
        page = item.funcargs.get("page", None)
        if page:
            step = report.when  # setup / call / teardown
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"Failure Screenshot ({step})",
                attachment_type=allure.attachment_type.PNG
            )


# allure generate ./allure-results --clean -o ./allure-report
# allure open ./allure-report

# we can use this command to generate and open the allure report after test execution is completed
# allure open ./allure-report
