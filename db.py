import json

import get_test_data
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_DIR

# Settingsfrom main

engine = create_engine(f'sqlite:///{DB_DIR}', echo=True) # should create first time


Base = declarative_base()

class Place(Base):
    __tablename__ = 'places'

    id = Column(String, primary_key=True)
    #timestamp = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    types = Column(String)
    current_popularity = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    popular_times = Column(String)

    def __init__(self, id, name):
        self.id = id
        self.name = name


Session = sessionmaker(bind=engine)
session = Session()
data = json.loads(get_test_data("ChIJNaccT7UcdkgRCnzTgAKK8k0"))
place = Place(data["id"], data["name"])
session.add(place)
session.commit()
session.close()



