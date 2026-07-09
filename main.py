from core.menu import Menu
from core.auth.selenium_session import setup_selenium_login
from core.config import SELENIUM_PROFILE

def main():

    if not SELENIUM_PROFILE.exists() or not any(SELENIUM_PROFILE.iterdir()):
        setup_selenium_login()

    menu = Menu()
    menu.run()


if __name__ == "__main__":
    main()
