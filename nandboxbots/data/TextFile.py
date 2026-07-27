import json


class TextFile:
    __KEY_SIZE = "size"
    __KEY_ID = "id"

    size = None
    id = None

    def __init__(self, dictionary):
        self.size = int(dictionary[self.__KEY_SIZE]) if dictionary.get(self.__KEY_SIZE) is not None else None
        self.id = str(dictionary[self.__KEY_ID]) if dictionary.get(self.__KEY_ID) is not None else None

    def to_json_obj(self):

        dictionary = {}

        if self.size is not None:
            dictionary[self.__KEY_SIZE] = self.size
        if self.id is not None:
            dictionary[self.__KEY_ID] = self.id

        return json.dumps(dictionary), dictionary
