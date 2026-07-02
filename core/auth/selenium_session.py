from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from core.config import URL


def start_browser_session():
    options = Options()

    options.add_argument(r"--user-data-dir=selenium_profile")
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

    print("\n" + "=" * 70)
    print(message)
    print("=" * 70 + "\n")

    input("\nPress ENTER after completing login...")

    browser.quit()
