#!/usr/bin/python3
""" Subclass of BaseModel in charge of saving the place information"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class Used to represent an apartment/house/room
        Attributes
        ----------
        city_id: str
            it will be the City.id
        user_id: str
            it will be the User.id
        name: str
            name of the place
        description: str
            description of the apartment/house/room
        number_rooms: int
            number of rooms avaliable
        number_bathrooms: int
            number of bathrooms avaliable
        max_guest: int
            number of guest the place can have
        price_by_night: int
            the price of the night represent with an int
        latitude: flt
            the latitude of the place
        longitude: flt
            the longitude of the place
        amenity_ids: list of string
            it will be the list of Amenity.id later
            """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
