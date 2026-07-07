from selenium.webdriver.common.by import By
from core.relist.image_downloader import save_images


def extract_listing_data(browser, listing_id):

    listing = {}

    inputs = browser.find_elements(By.CSS_SELECTOR, "input[readonly]")

    for field in inputs:
        key = field.get_attribute("name")
        value = field.get_attribute("value")

        if value:
            listing[key] = value

    listing["title"] = browser.find_element(
        By.CSS_SELECTOR, "[data-testid='title--input']"
    ).get_attribute("value")

    listing["description"] = browser.find_element(
        By.CSS_SELECTOR, "[data-testid='description--input']"
    ).get_attribute("value")

    listing["price"] = (
        browser.find_element(By.CSS_SELECTOR, "[data-testid='price-input--input']")
        .get_attribute("value")
        .replace("€", "")
        .replace("\xa0", "")
        .strip()
    )

    selected = browser.find_element(
    By.CSS_SELECTOR,
    "input[type='radio'][checked]"
)

    package_size = selected.find_element(
        By.XPATH,
        "./ancestor::div[contains(@data-testid, '--cell')]"
    ).get_attribute("data-testid")

    listing["package_size"] = package_size.split("-")[0]

    images = browser.find_elements(
    By.CSS_SELECTOR,
    "[data-testid^='image-wrapper-'] img"
)

    image_urls = [
        img.get_attribute("src")
        for img in images
    ]

    listing["images"] = save_images(image_urls, listing_id)

    return listing
