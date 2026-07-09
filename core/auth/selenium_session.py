from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from core.config import SELENIUM_PROFILE,URL
from core.terminal import console




def setup_selenium_login():
    options = Options()

    options.add_argument(f"--user-data-dir={SELENIUM_PROFILE}")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    browser = webdriver.Chrome(options=options)

    browser.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    browser.get(URL)

    message = """
    First-time login required

    A browser window will open.
    Please log in and complete any verification steps.

    Note: Only required on first run.
    """

    print("\n" + "=" * 60)
    print(message)
    print("=" * 60 + "\n")

    input("\nPress ENTER after completing login...")
    console.clear()

    browser.quit()