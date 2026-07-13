import pytest
import allure

from pages.login_page import LoginPage

@allure.title("Sample")
@allure.description("To test the valid and invalid scenario")
def test_login(page):

    obj = LoginPage(page)  # class constructor , create the object for the class
    obj.login("testuser","testuser123")  # using the object we are calling the method