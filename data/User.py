import json

from data.Photo import Photo


class User:
    KEY_ID = "id"
    KEY_NAME = "name"
    KEY_TERMINAL = "terminal"
    KEY_TYPE = "type"
    KEY_IS_BOT = "is_bot"
    KEY_VERSION = "version"
    KEY_LAST_SEEN = "last_seen"
    KEY_STATUS = "status"
    KEY_PHOTO = "photo"
    KEY_PROFILE = "profile"
    KEY_SHORT_NAME = "short_name"

    id = None
    name = None
    version = None
    terminal = None
    type = None
    is_bot = False
    last_seen = None
    status = None
    profile = None
    photo = None
    short_name = None

    def __init__(self, dictionary):
        # print(str(dictionary))
        self.id = str(dictionary[self.KEY_ID]) if self.KEY_ID in dictionary.keys() else None
        self.name = str(dictionary[self.KEY_NAME]) if self.KEY_NAME in dictionary.keys() else None
        self.version = str(dictionary[self.KEY_VERSION]) if self.KEY_VERSION in dictionary.keys() else None
        self.terminal = str(dictionary[self.KEY_TERMINAL]) if self.KEY_TERMINAL in dictionary.keys() else None
        self.type = str(dictionary[self.KEY_TYPE]) if self.KEY_TYPE in dictionary.keys() else None
        self.is_bot = bool(dictionary[self.KEY_IS_BOT]) if self.KEY_IS_BOT in dictionary.keys() else None
        self.last_seen = str(dictionary[self.KEY_LAST_SEEN]) if self.KEY_LAST_SEEN in dictionary.keys() else None
        self.status = str(dictionary[self.KEY_STATUS]) if self.KEY_STATUS in dictionary.keys() else None
        self.profile = str(dictionary[self.KEY_PROFILE]) if self.KEY_PROFILE in dictionary.keys() else None

        self.photo = Photo(dictionary.get(self.KEY_PHOTO, {}))

        self.short_name = str(dictionary[self.KEY_SHORT_NAME]) if self.KEY_SHORT_NAME in dictionary.keys() else None

    def to_json_obj(self):
        dictionary = {}

        if self.id is not None:
            dictionary[self.KEY_ID] = self.id
        if self.name is not None:
            dictionary[self.KEY_NAME] = self.name
        if self.version is not None:
            dictionary[self.KEY_VERSION] = self.version
        if self.terminal is not None:
            dictionary[self.KEY_TERMINAL] = self.terminal
        if self.type is not None:
            dictionary[self.KEY_TYPE] = self.type
        if self.is_bot is not None:
            dictionary[self.KEY_IS_BOT] = self.is_bot
        if self.last_seen is not None:
            dictionary[self.KEY_LAST_SEEN] = self.last_seen
        if self.status is not None:
            dictionary[self.KEY_STATUS] = self.status
        if self.profile is not None:
            dictionary[self.KEY_PROFILE] = self.profile
        if self.photo is not None:
            _, photo_dict = self.photo.to_json_obj()
            dictionary[self.KEY_PHOTO] = photo_dict
        if self.short_name is not None:
            dictionary[self.KEY_SHORT_NAME] = self.short_name

        return json.dumps(dictionary), dictionary
