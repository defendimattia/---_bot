import json
import os


def load_listing_data(listing_id):

    path = os.path.join("temp", str(listing_id), "data.json")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
