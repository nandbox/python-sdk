import json

from data.Thumbnail import Thumbnail


class Gif:
    KEY_ID = "id"
    KEY_WIDTH = "width"
    KEY_HEIGHT = "height"
    KEY_SIZE = "size"
    KEY_THUMBNAIL = "thumbnail"

    id = None
    width = None
    height = None
    size = None
    thumbnail = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.KEY_ID]) if self.KEY_ID in dictionary.keys() else None
        self.width = int(dictionary[self.KEY_WIDTH]) if self.KEY_WIDTH in dictionary.keys() else None
        self.height = int(dictionary[self.KEY_HEIGHT]) if self.KEY_HEIGHT in dictionary.keys() else None
        self.size = int(dictionary[self.KEY_SIZE]) if self.KEY_SIZE in dictionary.keys() else None
        self.thumbnail = Thumbnail(dictionary.get(self.KEY_THUMBNAIL, {}))

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
            _, thumbnail_dict = self.thumbnail.to_json_obj()
            dictionary[self.KEY_THUMBNAIL] = thumbnail_dict

        return json.dumps(dictionary), dictionary
