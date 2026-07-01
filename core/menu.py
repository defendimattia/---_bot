from core.terminal import console
from core.config import TITLE

class Menu:

    def run(self):

        while True:

            print(f"\n===== {TITLE} Bot =====")
            print("1. Visualizza annunci")
            print("2. Ripubblica annunci")
            print("3. Esci")

            scelta = input("\nScelta: ")

            if scelta == "1":
                self.show_listings()

            elif scelta == "2":
                self.republish_listing()

            elif scelta == "3":
                break

            else:
                console.clear()
                console.print("[bold][red]Scelta non valida[/red][/bold]\n")
