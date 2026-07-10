import os
from selenium.webdriver.common.by import By


def upload_images(browser, image_folder):

    image_files = []

    files = [
        f
        for f in os.listdir(image_folder)
        if f.lower().endswith((".jpg"))
    ]

    files.sort(key=lambda x: int(os.path.splitext(x)[0]))

    for filename in files:
        image_files.append(os.path.abspath(os.path.join(image_folder, filename)))

    if not image_files:
        raise Exception("No images found")

    file_input = browser.find_element(
        By.CSS_SELECTOR, "[data-testid='add-photos-input']"
    )

    file_input.send_keys("\n".join(image_files))
