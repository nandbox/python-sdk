import json

from data.Thumbnail import Thumbnail


class Sticker:
    KEY_ID = "id"
    KEY_WIDTH = "width"
    KEY_HEIGHT = "height"
    KEY_SIZE = "size"
    KEY_THUMBNAIL = "thumbnail"

    id = None
    width = None
    height = None
    thumbnail = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.KEY_ID])
        self.width = int(dictionary[self.KEY_WIDTH])
        self.height = int(dictionary[self.KEY_HEIGHT])
        self.size = int(dictionary[self.KEY_SIZE])
        self.thumbnail = Thumbnail(dictionary[self.KEY_THUMBNAIL]) if dictionary[
                                                                          self.KEY_THUMBNAIL] is not None else None

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

        return json.dumps(dictionary), dictionary
