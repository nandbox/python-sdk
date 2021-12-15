import json


class Location:
    KEY_NAME = "name"
    KEY_DETAILS = "details"
    KEY_LONGITUDE = "longitude"
    KEY_LATITUDE = "latitude"

    longitude = None
    latitude = None
    name = None
    details = None

    def __init__(self, dictionary):
        self.name = str(dictionary[self.KEY_NAME]) if self.KEY_NAME in dictionary.keys() else None
        self.details = str(dictionary[self.KEY_DETAILS]) if self.KEY_DETAILS in dictionary.keys() else None
        self.longitude = str(dictionary[self.KEY_LONGITUDE]) if self.KEY_LONGITUDE in dictionary.keys() else None
        self.latitude = str(dictionary[self.KEY_LATITUDE]) if self.KEY_LATITUDE in dictionary.keys() else None

    def to_json_obj(self):

        dictionary = {}

        if self.name is not None:
            dictionary[self.KEY_NAME] = self.name
        if self.details is not None:
            dictionary[self.KEY_DETAILS] = self.details
        if self.longitude is not None:
            dictionary[self.KEY_LONGITUDE] = self.longitude
        if self.latitude is not None:
            dictionary[self.KEY_LATITUDE] = self.latitude

        return json.dumps(dictionary), dictionary
