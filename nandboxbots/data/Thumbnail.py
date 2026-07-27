import json


class Thumbnail:
    __KEY_ID = "id"
    __KEY_WIDTH = "width"
    __KEY_HEIGHT = "height"

    id = None
    width = None
    height = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.__KEY_ID]) if dictionary.get(self.__KEY_ID) is not None else None
        self.width = int(dictionary[self.__KEY_WIDTH]) if dictionary.get(self.__KEY_WIDTH) is not None else None
        self.height = int(dictionary[self.__KEY_HEIGHT]) if dictionary.get(self.__KEY_HEIGHT) is not None else None

    def to_json_obj(self):
        dictionary = {}

        if self.id is not None:
            dictionary[self.__KEY_ID] = self.id
        if self.width is not None:
            dictionary[self.__KEY_WIDTH] = self.width
        if self.height is not None:
            dictionary[self.__KEY_HEIGHT] = self.height

        return json.dumps(dictionary), dictionary

    def to_dict(self):
        return {
            self.__KEY_ID: self.id,
            self.__KEY_WIDTH: self.width,
            self.__KEY_HEIGHT: self.height
        }
