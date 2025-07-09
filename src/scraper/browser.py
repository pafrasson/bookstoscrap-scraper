from playwright.sync_api import sync_playwright


def start_browser(headless=True):
    """
    Open the browser window
    :param headless: True
    :return: playwright, browser, context, page
    """
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context()
    page = context.new_page()
    return playwright, browser, context, page
