import json


class Result:
    KEY_ID = "id"
    KEY_CAPTION = "caption"
    KEY_TITLE = "title"
    KEY_DESCRIPTION = "description"
    KEY_URL = "url"
    KEY_TYPE = "type"
    KEY_THUMB_URL = "thumb_url"
    KEY_WIDTH = "width"
    KEY_HEIGHT = "height"

    id = None
    caption = None
    title = None
    description = None
    url = None
    type = None
    thumb_url = None
    width = None
    height = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.KEY_ID]) if self.KEY_ID in dictionary.keys() else None
        self.caption = str(dictionary[self.KEY_CAPTION]) if self.KEY_CAPTION in dictionary.keys() else None
        self.title = str(dictionary[self.KEY_TITLE]) if self.KEY_TITLE in dictionary.keys() else None
        self.description = str(dictionary[self.KEY_DESCRIPTION]) if self.KEY_DESCRIPTION in dictionary.keys() else None
        self.url = str(dictionary[self.KEY_URL]) if self.KEY_URL in dictionary.keys() else None
        self.type = str(dictionary[self.KEY_TYPE]) if self.KEY_TYPE in dictionary.keys() else None
        self.thumb_url = str(dictionary[self.KEY_THUMB_URL]) if self.KEY_THUMB_URL in dictionary.keys() else None
        self.width = int(dictionary[self.KEY_WIDTH]) if self.KEY_WIDTH in dictionary.keys() else None
        self.height = int(dictionary[self.KEY_HEIGHT]) if self.KEY_HEIGHT in dictionary.keys() else None

    def to_json_obj(self):

        dictionary = {}

        if self.id is not None:
            dictionary[self.KEY_ID] = self.id
        if self.caption is not None:
            dictionary[self.KEY_CAPTION] = self.caption
        if self.title is not None:
            dictionary[self.KEY_TITLE] = self.title
        if self.description is not None:
            dictionary[self.KEY_DESCRIPTION] = self.description
        if self.url is not None:
            dictionary[self.KEY_URL] = self.url
        if self.type is not None:
            dictionary[self.KEY_TYPE] = self.type
        if self.thumb_url is not None:
            dictionary[self.KEY_THUMB_URL] = self.thumb_url
        if self.width is not None:
            dictionary[self.KEY_WIDTH] = self.width
        if self.height is not None:
            dictionary[self.KEY_HEIGHT] = self.height

        return json.dumps(dictionary), dictionary
