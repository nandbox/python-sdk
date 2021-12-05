import json


class Audio:
    KEY_ID = "id"
    KEY_TITLE = "title"
    KEY_PERFORMER = "performer"
    KEY_SIZE = "size"
    KEY_DURATION = "duration"

    id = None
    title = None
    performer = None
    size = None
    duration = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.KEY_ID])
        self.title = str(dictionary[self.KEY_TITLE])
        self.performer = str(dictionary[self.KEY_PERFORMER])
        self.size = int(dictionary[self.KEY_SIZE])
        self.duration = int(dictionary[self.KEY_DURATION])

    def to_json_obj(self):

        dictionary = {}

        if self.id is not None:
            dictionary[self.KEY_ID] = self.id
        if self.title is not None:
            dictionary[self.KEY_TITLE] = self.title
        if self.performer is not None:
            dictionary[self.KEY_PERFORMER] = self.performer
        if self.size is not None:
            dictionary[self.KEY_SIZE] = self.size
        if self.duration is not None:
            dictionary[self.KEY_DURATION] = self.duration

        return json.dumps(dictionary), dictionary
