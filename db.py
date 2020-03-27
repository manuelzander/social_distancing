import logging
import sqlite3
import sys
import traceback

import coloredlogs
import pandas as pd
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from config import DB_DIR, TABLE_NAME

# Settings
# Logs
logger = logging.getLogger(__name__)

# Database
Base = declarative_base()


class Place(Base):
    __tablename__ = "places"

    id = Column(String, primary_key=True)
    timestamp = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    types = Column(String)
    current_popularity = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    popular_times = Column(String)

    def __init__(
        self,
        id,
        timestamp,
        name,
        address,
        types,
        current_popularity,
        latitude,
        longitude,
        popular_times,
    ):
        self.id = id
        self.timestamp = timestamp
        self.name = name
        self.address = address
        self.types = types
        self.current_popularity = current_popularity
        self.latitude = latitude
        self.longitude = longitude
        self.popular_times = popular_times


def read_data_from_db():
    try:
        connection = sqlite3.connect(DB_DIR)
        df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME}", connection)
        connection.close()
        logger.info(f"Success reading table {TABLE_NAME} from database {DB_DIR}")
        return df
    except Exception as e:
        logger.error(f"Error reading table {TABLE_NAME} from database {DB_DIR}:\n{e}")
        traceback.print_exc(file=sys.stdout)
        raise SystemExit
