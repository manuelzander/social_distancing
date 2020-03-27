#!/usr/bin/env python

import logging
import os
import sys
import traceback

import coloredlogs
import numpy as np
import pandas as pd
import streamlit as st

from config import DB_DIR, ROOT_DIR
from db import read_data_from_db

# Settings
# Logs
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")


# TO-DO: Implement caching
def load_data():
    # Get data from database
    data = read_data_from_db()

    # Convert unix ts into date
    data["date"] = pd.to_datetime(data["timestamp"], unit="s")
    return data


def main():
    st.title("Social distancing measures in London")

    data = load_data()
    if st.checkbox("Show raw data"):
        st.subheader("Raw data")
        st.dataframe(data)
        st.success("Successfully loaded data!")

    st.subheader("Mapping popularity of tube stations")
    midpoint = (np.average(data["latitude"]), np.average(data["longitude"]))

    st.deck_gl_chart(
        viewport={
            "latitude": midpoint[0],
            "longitude": midpoint[1],
            "zoom": 11,
            "pitch": 40,
        },
        layers=[
            {
                "type": "HexagonLayer",
                "data": data,
                "radius": 80,
                "elevationScale": 4,
                "elevationRange": [0, 1000],
                "pickable": True,
                "extruded": True,
            }
        ],
    )

    if st.checkbox("Like Balloons?"):
        st.balloons()


if __name__ == "__main__":
    logger.info(f"Running {__name__} in: {ROOT_DIR}")
    main()
