#!/usr/bin/env python

import argparse
import logging
import sys
import traceback

import coloredlogs
import pandas as pd

from config import ROOT_DIR, DATA_DIR


# Settings
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")


# def create_parser() -> argparse.ArgumentParser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--input_dir", default=DATA_DIR, help="Input directory to use")
#     return parser


def get_data():
    try:
        logger.info(f"Preparing data")
        data = None
        logger.info("Success preparing data")
        return data
    except Exception as e:
        logger.error(f"Error preparing data:\n{e}")
        traceback.print_exc(file=sys.stdout)
        raise SystemExit


def main():
    data = get_data()
    return data


if __name__ == "__main__":
    logger.info(f"Running: {ROOT_DIR}")
    main()
