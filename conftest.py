import os
from dotenv import load_dotenv
import pytest
from playwright.sync_api import sync_playwright

load_dotenv()

url = os.getenv("URL")

@pytest.fixture
def page():  # name of the fixture
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless
        page = browser.new_page()
        page.goto(url)
        page.set_default_timeout(25000)
        yield page
        browser.close()



