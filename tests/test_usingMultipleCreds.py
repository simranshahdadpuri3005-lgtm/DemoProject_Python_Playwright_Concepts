from playwright.sync_api import Page, expect
from pages.homePage import HomePage  
from pages.loginPage import LoginPage
import pytest
import json
from utils.readingJson import readJsonData

credentials = "testData\multipleCredntials.json"
testData = readJsonData(credentials)

@pytest.mark.parametrize("username,password", [
                                            (testData["validCredentials_QA"]["username"],testData["validCredentials_QA"]["password"]),
                                            (testData["validCredentials_Dev"]["username"],testData["validCredentials_Dev"]["password"]),
                                            (testData["InvalidCredentials"]["username"],testData["InvalidCredentials"]["password"])
                                               ]
                        )
def test_loginUsingValidCreds(page: Page, home_page, login_page,username,password):
    home_page.launchTheAmazonBrowser()
    home_page.hoverOnAccountsBtn()
    home_page.clickOnSignInBtn()



    login_page.enterEmailID(username)
    login_page.clickOnContinueBtn()
    login_page.enterPassword(password)
    login_page.clickOnContinueBtn()

    # this might give failures in the execution with the invalid usernames and password. but in this code we are just learining the parameterize concept
    

