import logging
import os
from pathlib import Path

import coloredlogs

# Settings
logger = logging.getLogger(__name__)

# Global constants
# Folders
ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = Path(os.path.join(ROOT_DIR, "data"))
TEST_DIR = Path(os.path.join(ROOT_DIR, "tests"))
DB_DIR = os.path.join(ROOT_DIR, "places.db")

# Files
TEST_DATA_FILE = os.path.join(ROOT_DIR, "test_data.jsonl")
API_KEY_FILE = os.path.join(ROOT_DIR, "api_keys.txt")
PLACE_ID_FILE = os.path.join(ROOT_DIR, "place_ids.txt")

# Other
TABLE_NAME = "places"


# Environment variables
class Config(object):
    def __init__(self):
        # Secrets
        # self.ACCOUNT = self._get_key_or_fail("ACCOUNT")
        # self.SECRET = self._get_key_or_fail("SECRET")
        pass

    @staticmethod
    def _get_key_or_fail(key):
        if key in os.environ:
            return os.environ.get(key)
        else:
            msg = f"{key} is not set in the environment and is required for the runtime"
            logger.error(msg)
            raise KeyError(msg)
