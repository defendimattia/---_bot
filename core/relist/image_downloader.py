import os
import requests


def save_images(image_urls, listing_id):
    folder = os.path.join("temp", str(listing_id))
    os.makedirs(folder, exist_ok=True)

    saved_files = []

    for index, url in enumerate(image_urls, start=1):
        ext = ".jpg"

        filename = os.path.join(folder, f"{index}{ext}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        with open(filename, "wb") as f:
            f.write(response.content)

        saved_files.append(filename)

    return saved_files
