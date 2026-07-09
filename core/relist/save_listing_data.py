import os


def save_listing_data(listing, listing_id):
    folder = os.path.join("temp", listing_id)
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, "data.txt")

    with open(filepath, "w", encoding="utf-8") as f:
        for key, value in listing.items():
            f.write(f"{key}: {value}\n")

    return filepath
