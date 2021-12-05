import json


class Thumbnail:
    KEY_ID = "id"
    KEY_WIDTH = "width"
    KEY_HEIGHT = "height"

    id = None
    width = None
    height = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.KEY_ID])
        self.width = int(dictionary[self.KEY_WIDTH])
        self.height = int(dictionary[self.KEY_HEIGHT])

    def to_json_obj(self):
        dictionary = {}

        if self.id is not None:
            dictionary[self.KEY_ID] = self.id
        if self.width is not None:
            dictionary[self.KEY_WIDTH] = self.width
        if self.height is not None:
            dictionary[self.KEY_HEIGHT] = self.height

        return json.dumps(dictionary), dictionary
