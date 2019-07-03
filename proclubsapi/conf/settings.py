import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
PLATAFORMS = os.getenv("PLATAFORMS").split()
INFOS = os.getenv("INFOS").split()
