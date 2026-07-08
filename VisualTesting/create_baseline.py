from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://amazon.in")
    page.wait_for_timeout(5000)
    # page.wait_for_load_state("networkidle")

    page.screenshot(path="baseline.png", full_page=True)

    print("Baseline screenshot captured")
