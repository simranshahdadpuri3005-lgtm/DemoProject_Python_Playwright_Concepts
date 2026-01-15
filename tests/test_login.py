from playwright.sync_api import Page, expect
import pytest
from conftest import home_page, login_page
from pages.homePage import HomePage  
#Homepage is class name
#homepage is python file inside pages folder
from pages.loginPage import LoginPage
import json
from utils.readingJson import readJsonData
import os


credentials = "testData/multipleCredntials.json"
testData = readJsonData(credentials)

# @pytest.mark.dependency(name="login")  
# we are creating a dependency with the name login, and use it when test_loginUsingValidCreds is a
#  pre requisite for other tests

#@pytest.mark.order(0)
@pytest.mark.smoke()
#if we use the fixture from the conftest file, we can comment this test case and call the fixture in other test cases
@pytest.mark.parametrize("username,password", [("trainingplaywright@gmail.com","Welcome@04")])
def test_loginUsingValidCreds(page, home_page, login_page, username, password):
    home_page.launchTheAmazonBrowser()
    #home_page.hoverOnAccountsBtn()
    home_page.clickOnSignInBtn()
    login_page.enterEmailID(username)
    login_page.clickOnContinueBtn()
    login_page.enterPassword(password)
    login_page.clickOnContinueBtn()

    #code to handle the json file
    #with open(credentials) as f:
     #   testData = json.load(f)
    #print(testData)
    #print(testData["username"])
    #print(testData["password"])

#@pytest.mark.dependency(depends=["login"])
# above statement indicates that the below test case is dependent on the test case with name 
# login that is test_loginUsingValidCreds
#def test_validateTheVisibilityOfSwitchAccount(page: Page, home_page, loginUsingValidCreds): 
#home_page.hoverOnAccountsBtn()
#we are calling the fixture created for login using valid credentials as shown above or else the below  method
# when we are using the test case and not the fixture



@pytest.mark.order(1)
@pytest.mark.productCheckout()
def test_validateTheVisibilityOfSwitchAccount(page: Page, home_page):
    home_page.launchTheAmazonBrowser()
    home_page.hoverOnAccountsBtn()
    home_page.validateTheVisibilityOfSwitchAccount()

    # for this testcase to run successfully, the user should be logged in state 
    # and for that we can use the session scope in conftest file for page fixture