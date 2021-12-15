import json


class Data:
    KEY_PATTERN = "pattern"
    KEY_EXAMPLE = "example"

    pattern = None
    example = None

    def __init__(self, dictionary):
        self.pattern = str(dictionary[self.KEY_PATTERN]) if self.KEY_PATTERN in dictionary.keys() else None
        self.example = str(dictionary[self.KEY_EXAMPLE]) if self.KEY_EXAMPLE in dictionary.keys() else None

    def to_json_obj(self):

        dictionary = {}

        if self.pattern is not None:
            dictionary[self.KEY_PATTERN] = self.pattern
        if self.example is not None:
            dictionary[self.KEY_EXAMPLE] = self.example

        return json.dumps(dictionary), dictionary
