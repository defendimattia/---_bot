import os
import json


def save_listing_data(listing, listing_id):

    folder = os.path.join("temp", str(listing_id))
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, "data.json")

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(listing, f, ensure_ascii=False, indent=4)

    return filepath
