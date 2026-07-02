from rich.table import Table
from rich import box
from core.terminal import console
from core.parser import fetch_listings


def view_listings():
    listings = fetch_listings()

    with console.status("Creating results table..."):

        table = Table(
            box=box.ROUNDED,
            show_lines=True,
            expand=True,
        )

        table.add_column("#", justify="center")
        table.add_column("Title")
        table.add_column("Price", justify="right", style="green", width=10)

        for i, item in enumerate(listings, start=1):
            table.add_row(
                str(i),
                item["title"],
                item["price"]
            )

        console.print("✔ Table created", style="bold green")
        console.print(table)

    input("\nPress ENTER to return to menu...")