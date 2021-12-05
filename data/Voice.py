import json


class Voice:
    KEY_ID = "id"
    KEY_DURATION = "duration"
    KEY_SIZE = "size"

    id = None
    duration = None
    size = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.KEY_ID])
        self.duration = int(dictionary[self.KEY_DURATION])
        self.size = int(dictionary[self.KEY_SIZE])

    def to_json_obj(self):

        dictionary = {}

        if self.id is not None:
            dictionary[self.KEY_ID] = self.id
        if self.duration is not None:
            dictionary[self.KEY_DURATION] = self.duration
        if self.size is not None:
            dictionary[self.KEY_SIZE] = self.size

        return json.dumps(dictionary), dictionary
