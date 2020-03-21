#!/usr/bin/env python

import argparse
import json
import logging
import os
import sys
import traceback

import coloredlogs
import pandas as pd
import populartimes

from datetime import datetime
from itertools import cycle

from config import ROOT_DIR, DATA_DIR, TEST_DATA_FILE


# Settings
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")


# def create_parser() -> argparse.ArgumentParser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--input_dir", default=DATA_DIR, help="Input directory to use")
#     return parser


def get_test_data(id):
    try:
        data = pd.read_json(os.path.join(ROOT_DIR, TEST_DATA_FILE), lines=True)
        response = data[data["id"] == id].to_json(orient="records", lines=True)
        logger.info(
            f"Success reading file {TEST_DATA_FILE} and getting data for id {id}"
        )
        return response
    except Exception as e:
        logger.error(f"Error getting data:\n{e}")
        traceback.print_exc(file=sys.stdout)
        raise SystemExit


def call_api(api_key, place_id):
    logger.info(
        f"Calling populartimes API with api_key {api_key} and place_id {place_id}"
    )
    return populartimes.get_id(api_key, place_id)


def get_data():
    try:
        logger.info(f"Getting data")

        with open("api_keys.txt") as f:
            api_keys = cycle([key.strip() for key in f.readlines()])

        with open("place_ids.txt") as f:
            place_ids = [id.strip() for id in f.readlines()]

        # responses =  [json.dumps(call_api(next(api_keys), id)) for id in place_ids] # prod
        responses =  [get_test_data(id) for id in place_ids] # dev
        
        # df = pd.DataFrame(responses)

        # if "current_popularity" in response:
        # data = []
        # data["name"] = response["name"]
        # data["id"] = response["id"]
        # data["populartimes"][datetime.now().weekday()]["data"][datetime.now().hour] = response["populartimes"][datetime.now().weekday()]["data"][datetime.now().hour]
        # data["current_popularity"] = response["current_popularity"]

        logger.info(f"Success getting data")
        return True
    except Exception as e:
        logger.error(f"Error getting data:\n{e}")
        traceback.print_exc(file=sys.stdout)
        raise SystemExit


def main():
    data = get_data()
    return data


if __name__ == "__main__":
    logger.info(f"Running {__name__} in: {ROOT_DIR}")
    main()
