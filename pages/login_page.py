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
        self.header.click_login()
        self.username.fill(user)
        self.password.fill(pwd)
        self.click_login.click()