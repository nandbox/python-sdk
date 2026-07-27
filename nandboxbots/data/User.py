import json

from nandboxbots.data.Photo import Photo
from nandboxbots.util import Utils


class User:
    __KEY_ID = "id"
    __KEY_NAME = "name"
    __KEY_TERMINAL = "terminal"
    __KEY_TYPE = "type"
    __KEY_IS_BOT = "is_bot"
    __KEY_VERSION = "version"
    __KEY_LAST_SEEN = "last_seen"
    __KEY_STATUS = "status"
    __KEY_PHOTO = "photo"
    __KEY_PROFILE = "profile"
    __KEY_SHORT_NAME = "short_name"
    __KEY_LOGIN_ID = "login_id"

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
    loginId = None

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        # print(str(dictionary))
        self.id = str(dictionary[self.__KEY_ID]) if dictionary.get(self.__KEY_ID) is not None else None
        self.name = str(dictionary[self.__KEY_NAME]) if dictionary.get(self.__KEY_NAME) is not None else None
        self.version = str(dictionary[self.__KEY_VERSION]) if dictionary.get(self.__KEY_VERSION) is not None else None
        self.terminal = str(dictionary[self.__KEY_TERMINAL]) if dictionary.get(self.__KEY_TERMINAL) is not None else None
        self.type = str(dictionary[self.__KEY_TYPE]) if dictionary.get(self.__KEY_TYPE) is not None else None
        self.is_bot = Utils.to_bool(dictionary.get(self.__KEY_IS_BOT))
        self.last_seen = str(dictionary[self.__KEY_LAST_SEEN]) if dictionary.get(self.__KEY_LAST_SEEN) is not None else None
        self.status = str(dictionary[self.__KEY_STATUS]) if dictionary.get(self.__KEY_STATUS) is not None else None
        # Guarded on the value so an explicit null yields the "other" default
        # rather than the literal string "None".
        self.profile = str(dictionary[self.__KEY_PROFILE]) if dictionary.get(self.__KEY_PROFILE) is not None else "other"
        # Was gated on __KEY_PROFILE: a user with a profile but no photo called
        # Photo(None) and crashed, and a user with a photo but no profile lost it.
        self.photo = Photo(dictionary[self.__KEY_PHOTO]) if dictionary.get(self.__KEY_PHOTO) is not None else None
        self.short_name = str(dictionary[self.__KEY_SHORT_NAME]) if dictionary.get(self.__KEY_SHORT_NAME) is not None else None
        self.loginId = int(dictionary[self.__KEY_LOGIN_ID]) if dictionary.get(self.__KEY_LOGIN_ID) is not None else None


    def to_json_obj(self):
        dictionary = {}

        if self.id is not None:
            dictionary[self.__KEY_ID] = self.id
        if self.name is not None:
            dictionary[self.__KEY_NAME] = self.name
        if self.version is not None:
            dictionary[self.__KEY_VERSION] = self.version
        if self.terminal is not None:
            dictionary[self.__KEY_TERMINAL] = self.terminal
        if self.type is not None:
            dictionary[self.__KEY_TYPE] = self.type
        if self.is_bot is not None:
            dictionary[self.__KEY_IS_BOT] = self.is_bot
        if self.last_seen is not None:
            dictionary[self.__KEY_LAST_SEEN] = self.last_seen
        if self.status is not None:
            dictionary[self.__KEY_STATUS] = self.status
        if self.profile is not None:
            dictionary[self.__KEY_PROFILE] = self.profile
        if self.photo is not None:
            _, photo_dict = self.photo.to_json_obj()
            dictionary[self.__KEY_PHOTO] = photo_dict
        if self.short_name is not None:
            dictionary[self.__KEY_SHORT_NAME] = self.short_name
        if self.loginId is not None:
            dictionary[self.__KEY_LOGIN_ID] = self.loginId

        return json.dumps(dictionary), dictionary
    def to_dict(self):
        return {
            self.__KEY_ID: self.id,
            self.__KEY_NAME: self.name,
            self.__KEY_VERSION: self.version,
            self.__KEY_TERMINAL: self.terminal,
            self.__KEY_TYPE: self.type,
            self.__KEY_IS_BOT: self.is_bot,
            self.__KEY_LAST_SEEN: self.last_seen,
            self.__KEY_STATUS: self.status,
            self.__KEY_PROFILE: self.profile,
            self.__KEY_PHOTO: self.photo.to_dict() if self.photo else None,
            self.__KEY_SHORT_NAME: self.short_name,
            self.__KEY_LOGIN_ID: self.loginId
        }