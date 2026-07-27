import json


class Voice:
    __KEY_ID = "id"
    __KEY_DURATION = "duration"
    __KEY_SIZE = "size"

    id = None
    duration = None
    size = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.__KEY_ID]) if dictionary.get(self.__KEY_ID) is not None else None
        self.duration = int(dictionary[self.__KEY_DURATION]) if dictionary.get(self.__KEY_DURATION) is not None else None
        self.size = int(dictionary[self.__KEY_SIZE]) if dictionary.get(self.__KEY_SIZE) is not None else None

    def to_json_obj(self):

        dictionary = {}

        if self.id is not None:
            dictionary[self.__KEY_ID] = self.id
        if self.duration is not None:
            dictionary[self.__KEY_DURATION] = self.duration
        if self.size is not None:
            dictionary[self.__KEY_SIZE] = self.size

        return json.dumps(dictionary), dictionary
