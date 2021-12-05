import json


class PermanentUrl:
    KEY_FILE = "file"
    KEY_URL = "url"
    KEY_PARAM1 = "param1"

    file = None
    url = None
    param1 = None

    def __init__(self, dictionary):
        self.url = str(dictionary[self.KEY_URL])
        self.file = str(dictionary[self.KEY_FILE])
        self.param1 = str(dictionary[self.KEY_PARAM1])

    def to_json_obj(self):

        dictionary = {}

        if self.url is not None:
            dictionary[self.KEY_URL] = self.url
        if self.file is not None:
            dictionary[self.KEY_FILE] = self.file
        if self.param1 is not None:
            dictionary[self.KEY_PARAM1] = self.param1

        return json.dumps(dictionary), dictionary
