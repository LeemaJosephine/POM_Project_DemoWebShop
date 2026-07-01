import pytest

from pages.login_page import LoginPage
from utils.excel_reader import read_excel

test_data = read_excel("testdata\\TestData_Demo.xlsx","LoginData")

@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("username,password", test_data)
def test_login(page, username, password):

    obj = LoginPage(page)  # class constructor , create the object for the class
    obj.login(username,password)  # using the object we are calling the method