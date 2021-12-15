import json


class TextFile:
    KEY_SIZE = "size"
    KEY_ID = "id"

    size = None
    id = None

    def __init__(self, dictionary):
        self.size = int(dictionary[self.KEY_SIZE]) if self.KEY_SIZE in dictionary.keys() else None
        self.id = str(dictionary[self.KEY_ID]) if self.KEY_ID in dictionary.keys() else None

    def to_json_obj(self):

        dictionary = {}

        if self.size is not None:
            dictionary[self.KEY_SIZE] = self.size
        if self.id is not None:
            dictionary[self.KEY_ID] = self.id

        return json.dumps(dictionary), dictionary
