import os
from dotenv import load_dotenv

load_dotenv()

GRID_LENGTH = int(os.getenv("GRID_LENGTH"))
PAWNS_TO_ALIGN = int(os.getenv("PAWNS_TO_ALIGN"))