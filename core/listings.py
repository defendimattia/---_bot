from rich.table import Table
from core.terminal import console


def get_listings():
    return [
        {"id": 1, "title": "Nike Air Force", "price": 60},
        {"id": 2, "title": "PS4 Controller", "price": 25},
        {"id": 3, "title": "FIFA 24", "price": 30},
    ]


def view_listings():

    listings = get_listings()

    table = Table(title="My Listings")

    table.add_column("ID", justify="center")
    table.add_column("Title")
    table.add_column("Price", justify="right")

    for item in listings:
        table.add_row(str(item["id"]), item["title"], f"{item['price']}€")

    console.print(table)
    input("\nPress ENTER to return to menu...")
