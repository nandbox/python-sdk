import json

from outmessages.OutMessage import OutMessage


class LocationOutMessage(OutMessage):
    KEY_NAME = "name"
    KEY_DETAILS = "details"
    KEY_LONGITUDE = "longitude"
    KEY_LATITUDE = "latitude"

    longitude = None
    latitude = None
    name = None
    details = None

    def __init__(self):
        self.method = "sendLocation"

    def to_json_obj(self):
        _, dictionary = super(LocationOutMessage, self).to_json_obj()

        if self.name is not None:
            dictionary[self.KEY_NAME] = self.name
        if self.details is not None:
            dictionary[self.KEY_DETAILS] = self.details
        if self.latitude is not None:
            dictionary[self.KEY_LATITUDE] = self.latitude
        if self.longitude is not None:
            dictionary[self.KEY_LONGITUDE] = self.longitude

        return json.dumps(dictionary), dictionary

