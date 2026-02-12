import pytest
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger("LoginTest")

def test_login():

    logger.info("Starting Login Test")

    assert True

    logger.info("Login Test Completed")


@pytest.mark.parametrize("username,password,expected_text", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("wronguser", "wrongpass", "Your username is invalid!"),
    ("tomsmith", "wrongpass", "Your password is invalid!")
])

def test_login_scenarios(driver, username, password, expected_text):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(username, password)

    message = login_page.get_message_text()
    assert expected_text in message
    #assert "WRONG TEXT" in message #for failed test cases and checking screenshots to be added in reports folder

#to check if any test fails screenshot is being saved
def test_fail_example(driver):
    driver.get("https://google.com")
    assert False
