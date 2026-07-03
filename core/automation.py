from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def scroll_to_bottom(browser, timeout=5):
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            WebDriverWait(browser, timeout).until(
                lambda b: b.execute_script("return document.body.scrollHeight")
                > last_height
            )

            last_height = browser.execute_script("return document.body.scrollHeight")

        except TimeoutException:
            break
