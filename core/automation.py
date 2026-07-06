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
    elements = browser.find_elements(By.CSS_SELECTOR, "a, button, div, img")
    ActionChains(browser).move_to_element(random.choice(elements)).perform()
