from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://amazon.in")
    page.wait_for_timeout(7000)
    #page.wait_for_load_state("load")
    # page.wait_for_load_state("networkidle")

    page.screenshot(path="VisualTesting/current.png", full_page=True)

    browser.close()

    baseline = Image.open("VisualTesting/baseline.png")
    current = Image.open("VisualTesting/current.png")

    difference = ImageChops.difference(baseline, current)

    if difference.getbbox() is None:
        print("No difference")
    else:
        difference.save("VisualTesting/difference.png")