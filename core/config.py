import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

TITLE = os.getenv("TITLE")
URL = os.getenv("URL")
BASE_DIR = Path(__file__).resolve().parents[1]
SELENIUM_PROFILE = BASE_DIR / "selenium_profile"

