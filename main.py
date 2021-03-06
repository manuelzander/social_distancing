#!/usr/bin/env python

import json
import logging
import os
import sys
import time
import traceback
from itertools import cycle

import coloredlogs
import pandas as pd
import populartimes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import API_KEY_FILE, DB_DIR, PLACE_ID_FILE, ROOT_DIR, TEST_DATA_FILE
from db import Base, Place

# Settings
# Logs
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")

# Database
engine = create_engine(f"sqlite:///{DB_DIR}")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def get_test_data(place_id):
    try:
        data = pd.read_json(os.path.join(ROOT_DIR, TEST_DATA_FILE), lines=True)
        if len(data[data["id"] == place_id]):
            response = data[data["id"] == place_id].to_json(
                orient="records", lines=True
            )
            logger.info(
                f"Success reading file {TEST_DATA_FILE} and getting data for id {place_id}"
            )
            return response
        raise populartimes.crawler.PopulartimesException(
            "Google Places INVALID_REQUEST",
            "The query string is malformed, check if your formatting for lat/lng and radius is correct.",
        )
    except Exception as e:
        logger.error(f"Error getting data:\n{e}")
        traceback.print_exc(file=sys.stdout)
        raise SystemExit


def call_api(api_key, place_id):
    logger.info(
        f"Calling populartimes API with api_key {api_key} and place_id {place_id}"
    )
    return populartimes.get_id(api_key, place_id)


def commit_to_db(data):
    try:
        session = Session()
        place = Place(
            data["id"],
            data["timestamp"],
            data["name"],
            data["address"],
            ",".join(data["types"]),
            data["current_popularity"],
            data["coordinates"]["lat"],
            data["coordinates"]["lng"],
            str(data["populartimes"]),
        )
        session.add(place)
        session.commit()
        session.close()
        logger.info(f"Success commiting data:\n{data}")
    except Exception as e:
        logger.error(f"Error commiting data:\n{e}")
        traceback.print_exc(file=sys.stdout)
        raise SystemExit


def get_data():
    try:
        logger.info(f"Getting data")

        if not os.path.isfile(API_KEY_FILE) or not os.path.isfile(PLACE_ID_FILE):
            logger.error(
                f"API_KEY_FILE {API_KEY_FILE} or PLACE_ID_FILE {PLACE_ID_FILE} not found"
            )
            raise SystemExit

        with open(API_KEY_FILE) as f:
            api_keys = cycle([key.strip() for key in f.readlines() if key.strip()])

        with open(PLACE_ID_FILE) as f:
            place_ids = [
                place_id.strip().split(",")[0]
                for place_id in f.readlines()
                if place_id.strip()
            ]

        for place_id in place_ids:
            response = json.loads(
                json.dumps(call_api(next(api_keys), place_id))
            )  # prod
            # response = json.loads(get_test_data(place_id))  # dev

            if "current_popularity" in response:
                response["timestamp"] = time.time()
                commit_to_db(response)
            else:
                logger.warn(f"No current_popularity in response:\n{response}")

        logger.info(f"Success getting data")
        return True
    except Exception as e:
        logger.error(f"Error getting data:\n{e}")
        traceback.print_exc(file=sys.stdout)
        raise SystemExit


def main():
    return get_data()


if __name__ == "__main__":
    logger.info(f"Running {__name__} in: {ROOT_DIR}")
    main()
