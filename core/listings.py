from rich.table import Table
from rich import box
from core.terminal import console
from core.parser import fetch_listings


def view_listings():
    listings = fetch_listings()

    try:
        with console.status("Creating results table..."):

            table = Table(
                box=box.ROUNDED,
                show_lines=True,
                expand=True,
            )

            table.add_column("#", justify="center")
            table.add_column("Title")
            table.add_column("Price", justify="right", style="green", width=10)

            for item in listings:
                table.add_row(
                    item["short_id"],
                    item["title"],
                    item["price"]
                )

            console.print("✔ Table created", style="bold green")
            console.print(table)

    except Exception as e:
        console.print(f"❌ Error during creating table: {e}", style="bold red")


    input("\nPress ENTER to return to menu...")