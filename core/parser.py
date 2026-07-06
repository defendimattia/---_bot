from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from core.config import URL, SELENIUM_PROFILE
from core.terminal import console
from selenium.common.exceptions import NoSuchElementException
from core.automation import scroll_to_bottom


def fetch_listings():

    options = Options()

    options.add_argument(f"--user-data-dir={SELENIUM_PROFILE}")
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    try:
        with console.status("Starting browser and navigating to profile..."):

            browser = webdriver.Chrome(options=options)

            browser.execute_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            )

            browser.get(URL)

            wait = WebDriverWait(browser, 20)

            menu_button = wait.until(
                EC.element_to_be_clickable((By.ID, "user-menu-button"))
            )
            menu_button.click()

            profile_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Profilo"))
            )
            profile_link.click()

        console.print("✔ Browser started and profile reached", style="bold green")

    except Exception as e:
        console.print(f"❌ Error during browser navigation: {e}", style="bold red")
        browser.quit()
        return []

    try:
        with console.status("Loading and extracting items..."):

            wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "[data-testid='grid-item']")
                )
            )

            scroll_to_bottom(browser)

            items = browser.find_elements(By.CSS_SELECTOR, "[data-testid='grid-item']")

            listings = []

            for i, item in enumerate(items, start=1):

                try:
                    real_id = (
                        item.find_element(
                            By.CSS_SELECTOR, "a.new-item-box__overlay--clickable"
                        )
                        .get_attribute("href")
                        .split("/")[-1]
                    )

                    title = (
                        item.find_element(
                            By.CSS_SELECTOR, "a.new-item-box__overlay--clickable"
                        )
                        .get_attribute("title")
                        .split(",")[0]
                        .strip()
                    )

                    status = ""
                    try:
                        status = item.find_element(
                            By.CSS_SELECTOR, "[data-testid$='--status-text']"
                        ).text.strip()
                    except NoSuchElementException:
                        pass

                    if status:
                        title = f"[{status}] {title}"

                    price_el = item.find_element(
                        By.CSS_SELECTOR, "[data-testid$='--price-text']"
                    )

                    listings.append(
                        {
                            "id": real_id,
                            "short_id": str(i),
                            "title": title,
                            "price": price_el.text,
                            "status": status,
                        }
                    )

                except NoSuchElementException:
                    continue

        console.print(f"✔ Data extracted: {len(listings)} items", style="bold green")

    except Exception as e:
        console.print(f"❌ Error during browser navigation: {e}", style="bold red")
        return []

    finally:
        browser.quit()

    return listings
