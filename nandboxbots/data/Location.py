import json


class Location:
    __KEY_NAME = "name"
    __KEY_DETAILS = "details"
    __KEY_LONGITUDE = "longitude"
    __KEY_LATITUDE = "latitude"

    longitude = None
    latitude = None
    name = None
    details = None

    def __init__(self, dictionary):
        self.name = str(dictionary[self.__KEY_NAME]) if dictionary.get(self.__KEY_NAME) is not None else None
        self.details = str(dictionary[self.__KEY_DETAILS]) if dictionary.get(self.__KEY_DETAILS) is not None else None
        self.longitude = str(dictionary[self.__KEY_LONGITUDE]) if dictionary.get(self.__KEY_LONGITUDE) is not None else None
        self.latitude = str(dictionary[self.__KEY_LATITUDE]) if dictionary.get(self.__KEY_LATITUDE) is not None else None

    def to_json_obj(self):

        dictionary = {}

        if self.name is not None:
            dictionary[self.__KEY_NAME] = self.name
        if self.details is not None:
            dictionary[self.__KEY_DETAILS] = self.details
        if self.longitude is not None:
            dictionary[self.__KEY_LONGITUDE] = self.longitude
        if self.latitude is not None:
            dictionary[self.__KEY_LATITUDE] = self.latitude

        return json.dumps(dictionary), dictionary
