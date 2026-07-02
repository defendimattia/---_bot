from rich.table import Table
from core.terminal import console
from core.parser import fetch_listings

def view_listings():

    listings = fetch_listings()

    table = Table(title="My Listings")

    table.add_column("ID", justify="center")
    table.add_column("Title")
    table.add_column("Price", justify="right")

    for i, item in enumerate(listings, start=1):
        table.add_row(str(i), item.get("title", "N/A"), f"{item.get('price', 0)}€")

    console.print(table)
    input("\nPress ENTER to return to menu...")
