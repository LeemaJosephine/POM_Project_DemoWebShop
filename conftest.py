import os
from dotenv import load_dotenv
import pytest
from playwright.sync_api import sync_playwright
from pytest_metadata.plugin import metadata_key

load_dotenv()

url = os.getenv("URL")

def pytest_configure(config):
    config.stash[metadata_key] ["Project"] ="DemoWebShop"
    config.stash[metadata_key]["Browser"] ="Chrome"
    config.stash[metadata_key]["Tester"] ="Leema"

@pytest.fixture
def page():  # name of the fixture
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless
        context = browser.new_context(record_video_dir="Videos/")

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )
        page = context.new_page()
        page.goto(url)
        page.set_default_timeout(25000)
        yield page
        context.tracing.stop(path="traceviewer/trace.zip")
        context.close()
        browser.close()



