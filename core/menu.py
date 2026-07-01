from core.terminal import console
from core.config import TITLE
from core.listings import view_listings


class Menu:

    def run(self):

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
                view_listings()

            elif choice == "2":
                self.relist_listing()

            elif choice == "3":
                break

            else:
                show_error = True
                console.clear()
