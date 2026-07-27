import json


class Result:
    __KEY_ID = "id"
    __KEY_CAPTION = "caption"
    __KEY_TITLE = "title"
    __KEY_DESCRIPTION = "description"
    __KEY_URL = "url"
    __KEY_TYPE = "type"
    __KEY_THUMB_URL = "thumb_url"
    __KEY_WIDTH = "width"
    __KEY_HEIGHT = "height"

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
        self.id = str(dictionary[self.__KEY_ID]) if dictionary.get(self.__KEY_ID) is not None else None
        self.caption = str(dictionary[self.__KEY_CAPTION]) if dictionary.get(self.__KEY_CAPTION) is not None else None
        self.title = str(dictionary[self.__KEY_TITLE]) if dictionary.get(self.__KEY_TITLE) is not None else None
        self.description = str(dictionary[self.__KEY_DESCRIPTION]) if dictionary.get(self.__KEY_DESCRIPTION) is not None else None
        self.url = str(dictionary[self.__KEY_URL]) if dictionary.get(self.__KEY_URL) is not None else None
        self.type = str(dictionary[self.__KEY_TYPE]) if dictionary.get(self.__KEY_TYPE) is not None else None
        self.thumb_url = str(dictionary[self.__KEY_THUMB_URL]) if dictionary.get(self.__KEY_THUMB_URL) is not None else None
        self.width = int(dictionary[self.__KEY_WIDTH]) if dictionary.get(self.__KEY_WIDTH) is not None else None
        self.height = int(dictionary[self.__KEY_HEIGHT]) if dictionary.get(self.__KEY_HEIGHT) is not None else None

    def to_json_obj(self):

        dictionary = {}

        if self.id is not None:
            dictionary[self.__KEY_ID] = self.id
        if self.caption is not None:
            dictionary[self.__KEY_CAPTION] = self.caption
        if self.title is not None:
            dictionary[self.__KEY_TITLE] = self.title
        if self.description is not None:
            dictionary[self.__KEY_DESCRIPTION] = self.description
        if self.url is not None:
            dictionary[self.__KEY_URL] = self.url
        if self.type is not None:
            dictionary[self.__KEY_TYPE] = self.type
        if self.thumb_url is not None:
            dictionary[self.__KEY_THUMB_URL] = self.thumb_url
        if self.width is not None:
            dictionary[self.__KEY_WIDTH] = self.width
        if self.height is not None:
            dictionary[self.__KEY_HEIGHT] = self.height

        return json.dumps(dictionary), dictionary
