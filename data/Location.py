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
        self.name = str(dictionary[self.KEY_NAME])
        self.details = str(dictionary[self.KEY_DETAILS])
        self.longitude = str(dictionary[self.KEY_LONGITUDE])
        self.latitude = str(dictionary[self.KEY_LATITUDE])

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
