from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

# Settings
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
