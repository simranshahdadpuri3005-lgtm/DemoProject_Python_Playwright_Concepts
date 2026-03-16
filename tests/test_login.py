from playwright.sync_api import Page, expect
import pytest

# Import fixtures from conftest file
# Fixtures defined in conftest.py can be used directly in test cases
from conftest import home_page, login_page

# Import Page Object classes
from pages.homePage import HomePage  
#Homepage is class name
#homepage.py is python file inside pages folder


from pages.loginPage import LoginPage

import json
from utils.readingJson import readJsonData
import os

# Path to JSON file containing multiple credentials
credentials = "testData/multipleCredntials.json"
# Utility function reads the JSON file and converts it to Python dictionary
testData = readJsonData(credentials)


# -----------------------------------------------------------
# LOGIN TEST CASE
# -----------------------------------------------------------

@pytest.mark.dependency(name="login")  
# we are creating a dependency with the name login, and use it when test_loginUsingValidCreds is a
#  pre requisite for other tests

# Creating a dependency named "login"
# Other test cases can depend on this test by using:
# @pytest.mark.dependency(depends=["login"])

@pytest.mark.order(1)  # Order marker ensures this test runs first
@pytest.mark.smoke()   # Smoke marker indicates this test is part of the smoke test suite

#if we use the fixture from the conftest file, we can comment this test case and call the fixture in other test cases

# Parametrize allows running the same test with different data sets
# Here we are passing username and password as test parameters
@pytest.mark.parametrize("username,password", [("trainingplaywright@gmail.com","Welcome@04")])
def test_loginUsingValidCreds(page, home_page, login_page, username, password):
    home_page.launchTheAmazonBrowser()     # Launch Amazon application
    #home_page.hoverOnAccountsBtn()
    home_page.clickOnSignInBtn()        # Click Sign In button from the homepage
    login_page.enterEmailID(username)    # Enter email address on login page
    login_page.clickOnContinueBtn()    # Click Continue button
    login_page.enterPassword(password)     # Enter password
    login_page.clickOnContinueBtn()    # Click Sign In / Continue button



    # -------------------------------------------------------
    # Example: Reading credentials directly from JSON file
    # -------------------------------------------------------
    # This code is commented because we are using a utility
    # function (readJsonData) to read JSON instead

    # with open(credentials) as f:
    #     testData = json.load(f)
    
    # print(testData)
    # print(testData["username"])
    # print(testData["password"])


# -----------------------------------------------------------
# Dependency Example
# -----------------------------------------------------------
# The below marker indicates that the test depends on the
# successful execution of the test named "login"
# @pytest.mark.dependency(depends=["login"])

# "@pytest.mark.dependency(depends=["login"])" statement indicates that the below test case 
# is dependent on the test case with fixture name # login that is "test_loginUsingValidCreds"

# def test_validateTheVisibilityOfSwitchAccount(page: Page, home_page, loginUsingValidCreds): 
    # home_page.hoverOnAccountsBtn()

# we are calling the fixture created for login using valid credentials as shown above or else the below  method
# when we are using the test case and not the fixture


# -----------------------------------------------------------
# SWITCH ACCOUNT VISIBILITY TEST
# -----------------------------------------------------------

# for this testcase to run successfully, the user should be logged in state 
# and for that we can use the session scope in conftest file for page fixture

@pytest.mark.order(2)
@pytest.mark.productCheckout()
def test_validateTheVisibilityOfSwitchAccount(page: Page, home_page):
    home_page.launchTheAmazonBrowser()
    home_page.hoverOnAccountsBtn()
    home_page.validateTheVisibilityOfSwitchAccount()


# -----------------------------------------------------------
# IMPORTANT NOTE
# -----------------------------------------------------------

# For this test to pass successfully:
# 1. The user must be in logged-in state.
# 2. This can be achieved by:
#    - Using dependency marker
#    - Using a login fixture
#    - Using session scope in conftest.py for page fixture
#
# In this example, the test may intentionally fail # to demonstrate failed test reporting in HTML/Allure reports.