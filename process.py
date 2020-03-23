#!/usr/bin/env python

import logging
import os
import sys
import traceback

import coloredlogs
import pandas as pd

from config import ROOT_DIR, DB_DIR
from db import read_data_from_db

# Settings
# Logs
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")


def process():
    # Get data from database
    data =  read_data_from_db()

    # Convert unix ts into date
    data["date"] = pd.to_datetime(data['timestamp'], unit='s')
    print(data["date"].describe())


def main():
    return process()


if __name__ == "__main__":
    logger.info(f"Running {__name__} in: {ROOT_DIR}")
    main()
