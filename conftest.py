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

# def pytest_addoption(parser):
#     parser.addoption(  # method that registers a new command-line option
#         "--browser-name",
#         action="store",  # store the value the user is passing
#         default="chrome", # if the user does not specify the --browser option, pytest automatically uses chrome
#         help="Browser to run tests on"  # Description
#     )

@pytest.fixture(params=["chromium","firefox","webkit"])
def page(request):  # name of the fixture
    browser_name = request.config.getoption("--browser")

    with sync_playwright() as p:

        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)  # headless
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)

        else:
            browser = p.chromium.launch(headless=False)

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



