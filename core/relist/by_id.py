from selenium import webdriver
from core.config import URL, SELENIUM_PROFILE
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from core.relist.extract_listing_data import extract_listing_data
from core.terminal import console

def relist_by_id(listings):

    choice = int(input("Type IDs to relist: "))
    print("=" * 60)

    try:
        with console.status(" Extracting listing data..."):

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

            browser = webdriver.Chrome(options=options)

            browser.execute_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
                    )


            item_to_relist = listings[choice - 1]

            browser.get(URL + "/items/" + item_to_relist["id"])

            wait = WebDriverWait(browser, 20)

            edit_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='item-edit-button']"))
            )
            edit_button.click()

            data = extract_listing_data(browser, item_to_relist["id"])


            browser.quit()

        console.print("✔  Listing data extracted", style="bold green")

        print("\n")
        print(data)

        input("fine")

    except Exception as e:
        console.print(
            f"❌  Error while extracting listing data: {e}",
            style="bold red"
        )
        browser.quit()
        return
