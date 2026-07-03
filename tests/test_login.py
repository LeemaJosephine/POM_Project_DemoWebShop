import pytest
import allure

from pages.login_page import LoginPage
from utils.excel_reader import read_excel

test_data = read_excel("testdata\\TestData_Demo.xlsx","LoginData")

@allure.title("Login Test")
@allure.description("To test the valid and invalid scenario")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("username,password", test_data)
def test_login(page, username, password):

    obj = LoginPage(page)  # class constructor , create the object for the class
    obj.login(username,password)  # using the object we are calling the method