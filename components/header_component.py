class HeaderComponent:
    def __init__(self, page):
        self.page = page

        # Locator
        self.login_button = page.locator("#login2")
        self.home = page.get_by_role("link", name="Home")
        self.contact = page.get_by_role("link", name="Contact")
        self.about_us = page.get_by_role("link", name="About us")
        self.cart = page.get_by_role("link", name="Cart")
        self.sign_up = page.locator("#signup")

    # Methods
    def click_login(self):
        self.login_button.click()

    def click_home(self):
        self.home.click()

    def click_contact(self):
        self.contact.click()

    def click_about_us(self):
        self.about_us.click()

    def click_cart(self):
        self.cart.click()

    def click_sign_up(self):
        self.sign_up.click()

