import os
from pathlib import Path

ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = Path(os.path.join(ROOT_DIR, "data"))
TEST_DIR = Path(os.path.join(ROOT_DIR, "tests"))
TEST_DATA_FILE = "test_data.jsonl"
API_KEY_FILE = "api_keys.txt"
PLACE_ID_FILE = "place_ids.txt"

