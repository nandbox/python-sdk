import json


class Thumbnail:
    KEY_ID = "id"
    KEY_WIDTH = "width"
    KEY_HEIGHT = "height"

    id = None
    width = None
    height = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.KEY_ID]) if self.KEY_ID in dictionary.keys() else None
        self.width = int(dictionary[self.KEY_WIDTH]) if self.KEY_WIDTH in dictionary.keys() else None
        self.height = int(dictionary[self.KEY_HEIGHT]) if self.KEY_HEIGHT in dictionary.keys() else None

    def to_json_obj(self):
        dictionary = {}

        if self.id is not None:
            dictionary[self.KEY_ID] = self.id
        if self.width is not None:
            dictionary[self.KEY_WIDTH] = self.width
        if self.height is not None:
            dictionary[self.KEY_HEIGHT] = self.height

        return json.dumps(dictionary), dictionary
