import json


class ButtonQueryResult:
    KEY_LATITUDE = "latitude"
    KEY_LONGITUDE = "longitude"
    KEY_CONTACT = "contact"

    latitude = None
    longitude = None
    contact = None

    def __init__(self, dictionary):
        self.latitude = str(dictionary[self.KEY_LATITUDE]) if self.KEY_LATITUDE in dictionary.keys() else None
        self.longitude = str(dictionary[self.KEY_LONGITUDE]) if self.KEY_LONGITUDE in dictionary.keys() else None
        self.contact = str(dictionary[self.KEY_CONTACT]) if self.KEY_CONTACT in dictionary.keys() else None

    def to_json_obj(self):

        dictionary = {}

        if self.latitude is not None:
            dictionary[self.KEY_LATITUDE] = self.latitude
        if self.longitude is not None:
            dictionary[self.KEY_LONGITUDE] = self.longitude
        if self.contact is not None:
            dictionary[self.KEY_CONTACT] = self.contact

        return json.dumps(dictionary), dictionary

