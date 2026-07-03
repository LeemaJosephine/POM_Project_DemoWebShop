import allure
from components.header_component import HeaderComponent

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.header = HeaderComponent(page)

        # Locators
        self.username = page.locator("#loginusername")
        self.password = page.locator("#loginpassword")
        self.click_login = page.get_by_role("button", name="Log in")

    # Methods
    def login(self,user,pwd):
        with allure.step("Click login to login"):
            self.header.click_login()
        with allure.step("Enter username and password"):
            self.username.fill(user)
            self.password.fill(pwd)
        with allure.step("Click login"):
            self.click_login.click()

        self.page.screenshot(path="screenshots/image.png")

        allure.attach.file("screenshots/image.png",
                           name="Login Screenshot",
                           attachment_type=allure.attachment_type.PNG
                           )