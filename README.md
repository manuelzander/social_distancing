# social_distancing

![last-commit](https://img.shields.io/github/last-commit/manuelzander/social_distancing/master?logo=github&style=for-the-badge) ![issues-pr-raw](https://img.shields.io/github/issues-pr-raw/manuelzander/social_distancing?label=open%20prs&logo=github&style=for-the-badge) ![python](https://img.shields.io/badge/python-3.7-blue?style=for-the-badge&logo=python&logoColor=white) [![license](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Social distancing measures using Google Maps Places API for London tube stations.

## Prerequisites 🔧⚙️

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

The code is run and tested with Python 3.7.6 on macOS 10.14.6.

### Environment

Clone the repo to your local machine.

Create a virtual environment for Python 3 with:

    pip3 install virtualenv
    virtualenv -p python3 env

Activate the virtual environment with:

    source env/bin/activate

Install the required Python packages with:

    pip3 install -r requirements.txt

If you incur any error, deactivate the virtualenv (type `deactivate`), start it again, and repeat the previous step.

### Place IDs

The `place_ids.txt` file contains `place_ids` and names, for instance:

    ChIJNaccT7UcdkgRCnzTgAKK8k0,Aldgate East Station
    ChIJsUs1REwDdkgRX_9hC2x9f8U,Liverpool Street Station

For more information check [here](https://developers.google.com/places/web-service/place-id).

### Google Maps Places API keys

Create an `api_keys.txt` file containing `keys` (one per line).
For more information check [here](https://developers.google.com/places/web-service/get-api-key).

## The fun part 🎉🚀

### Data collection

Query the Google Maps Places API for all `place_ids` and store the data:

    python3 main.py

This creates a database `places.db`, which can be opened by running `sqlite3` followed by `.open places.db`.

A record looks like this:

    {'id': 'ChIJsUs1REwDdkgRX_9hC2x9f8U', 'name': 'Liverpool Street Station', 'address': 'Liverpool St, London EC2M 7PY, UK', 'types': ['train_station', 'transit_station', 'point_of_interest', 'establishment'], 'coordinates': {'lat': 51.51875159999999, 'lng': -0.08143740000000001}, 'rating': 4.2, 'rating_n': 1056, 'international_phone_number': '+44 345 711 4141', 'current_popularity': 3, 'populartimes': [{'name': 'Monday', 'data': [2, 1, 1, 1, 0, 4, 11, 20, 28, 30, 27, 27, 35, 37, 36, 47, 65, 79, 80, 67, 48, 28, 14, 5]}, {'name': 'Tuesday', 'data': [1, 0, 0, 0, 0, 4, 12, 22, 30, 30, 25, 25, 34, 37, 37, 47, 60, 70, 71, 63, 48, 33, 19, 9]}, {'name': 'Wednesday', 'data': [3, 1, 0, 0, 2, 5, 9, 14, 19, 25, 29, 31, 30, 27, 26, 36, 67, 97, 89, 52, 27, 24, 23, 15]}, {'name': 'Thursday', 'data': [5, 0, 0, 0, 2, 5, 10, 16, 23, 30, 34, 36, 34, 30, 30, 42, 69, 93, 90, 61, 35, 28, 27, 19]}, {'name': 'Friday', 'data': [8, 1, 0, 0, 3, 6, 10, 16, 22, 29, 35, 39, 39, 38, 38, 49, 75, 100, 91, 59, 35, 30, 31, 26]}, {'name': 'Saturday', 'data': [16, 7, 2, 1, 1, 1, 3, 7, 13, 20, 26, 31, 34, 35, 35, 36, 36, 36, 34, 31, 27, 23, 19, 15]}, {'name': 'Sunday', 'data': [10, 7, 3, 1, 1, 2, 3, 5, 9, 14, 19, 24, 28, 30, 31, 31, 30, 29, 25, 21, 15, 10, 6, 4]}], 'timestamp': 1584899728.03687}

The goal is to create interactive dashboards/maps of London based on `current_popularity` and `populartimes`.

### Data visualization

We are using the Python `streamlit` module for our interactive dashboards.
For more information check [here](https://docs.streamlit.io/).

To start the app on http://localhost:8501/ run:

    streamlit run app.py
