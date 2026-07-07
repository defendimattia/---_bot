import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


def scroll_to_bottom(browser, timeout=5):
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        random_mouse_move(browser)
        time.sleep(random.uniform(1, 3))

        try:
            WebDriverWait(browser, timeout).until(
                lambda b: b.execute_script("return document.body.scrollHeight")
                > last_height
            )

            last_height = browser.execute_script("return document.body.scrollHeight")

        except TimeoutException:
            break


def random_mouse_move(browser):
    elements = browser.find_elements(By.CSS_SELECTOR, "a, button, img")

    visible_elements = []

    for element in elements:
        try:
            if (
                element.is_displayed()
                and element.size["width"] > 0
                and element.size["height"] > 0
            ):
                visible_elements.append(element)
        except:
            pass

    if not visible_elements:
        return

    element = random.choice(visible_elements)

    try:
        ActionChains(browser).move_to_element(element).pause(
            random.uniform(0.2, 0.8)
        ).perform()
    except Exception:
        pass
