import json


class ButtonQueryResult:
    __KEY_LATITUDE = "latitude"
    __KEY_LONGITUDE = "longitude"
    __KEY_CONTACT = "contact"

    latitude = None
    longitude = None
    contact = None

    def __init__(self, dictionary):
        self.latitude = str(dictionary[self.__KEY_LATITUDE]) if dictionary.get(self.__KEY_LATITUDE) is not None else None
        self.longitude = str(dictionary[self.__KEY_LONGITUDE]) if dictionary.get(self.__KEY_LONGITUDE) is not None else None
        self.contact = str(dictionary[self.__KEY_CONTACT]) if dictionary.get(self.__KEY_CONTACT) is not None else None

    def to_json_obj(self):

        dictionary = {}

        if self.latitude is not None:
            dictionary[self.__KEY_LATITUDE] = self.latitude
        if self.longitude is not None:
            dictionary[self.__KEY_LONGITUDE] = self.longitude
        if self.contact is not None:
            dictionary[self.__KEY_CONTACT] = self.contact

        return json.dumps(dictionary), dictionary

