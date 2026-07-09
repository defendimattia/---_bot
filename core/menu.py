from core.terminal import console
from core.config import TITLE
from core.listings import view_listings
from core.relist.by_id import relist_by_id
from core.parser import fetch_listings

class Menu:

    def run(self):

        console.clear()
        listings = fetch_listings()

        show_error = False

        while True:

            console.clear()
            console.print("[bold green]" + TITLE.replace("\\n", "\n") + "[/bold green]")
            print("=" * 60)
            print("1. View listings")
            print("2. Relist listings")
            print("3. Exit")
            print("=" * 60)

            if show_error:
                console.print("[bold red]Invalid choice[/bold red]\n")
                show_error = False

            choice = input("\nChoice: ")

            if choice == "1":

                console.clear()
                view_listings(listings)

            elif choice == "2":
                while True:

                    console.clear()
                    console.print("\n[bold]Relist options:[/bold]")
                    print("=" * 60)
                    print("1. Relist by ID")
                    print("2. Relist last N items")
                    print("3. Exit")
                    print("=" * 60)

                    if show_error:
                        console.print("[bold red]Invalid choice[/bold red]\n")
                        show_error = False

                    choice = input("\nChoice: ")

                    if choice == "1":
                        console.clear()
                        relist_by_id(listings)

                    elif choice == "2":
                        pass

                    elif choice == "3":
                        break

                    else:
                        show_error = True
                        console.clear()

            elif choice == "3":
                break

            else:
                show_error = True
                console.clear()
