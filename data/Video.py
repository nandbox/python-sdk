import json

from data.Thumbnail import Thumbnail


class Video:
    KEY_ID = "id"
    KEY_WIDTH = "width"
    KEY_HEIGHT = "height"
    KEY_SIZE = "size"
    KEY_THUMBNAIL = "thumbnail"
    KEY_DURATION = "duration"

    id = None
    width = None
    height = None
    size = None
    thumbnail = None
    duration = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.KEY_ID])
        self.width = int(dictionary[self.KEY_WIDTH])
        self.height = int(dictionary[self.KEY_HEIGHT])
        self.size = int(dictionary[self.KEY_SIZE])
        self.thumbnail = Thumbnail(dictionary[self.KEY_THUMBNAIL]) if dictionary[self.KEY_THUMBNAIL] is not None else None
        self.duration = int(dictionary[self.KEY_DURATION])

    def to_json_obj(self):

        dictionary = {}

        if self.id is not None:
            dictionary[self.KEY_ID] = self.id
        if self.width is not None:
            dictionary[self.KEY_WIDTH] = self.width
        if self.height is not None:
            dictionary[self.KEY_HEIGHT] = self.height
        if self.size is not None:
            dictionary[self.KEY_SIZE] = self.size
        if self.thumbnail is not None:
            dictionary[self.KEY_THUMBNAIL] = self.thumbnail
        if self.duration is not None:
            dictionary[self.KEY_DURATION] = self.duration

        return json.dumps(dictionary), dictionary
