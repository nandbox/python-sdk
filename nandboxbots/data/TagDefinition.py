import json

from nandboxbots.util import Utils


class TagDefinition:
    __KEY_NAME = "name"
    __KEY_DESCRIPTION = "description"
    __KEY_ID = "id"
    __KEY_ISPRIVATE = "isPrivate"

    name = None
    description = None
    id = None
    is_private = None

    def __init__(self, dictionary):

        self.id = str(dictionary[self.__KEY_ID]) if dictionary.get(self.__KEY_ID) is not None else None
        self.name = str(dictionary[self.__KEY_NAME]) if dictionary.get(self.__KEY_NAME) is not None else None
        self.description = str(dictionary[self.__KEY_DESCRIPTION]) if dictionary.get(self.__KEY_DESCRIPTION) is not None else None
        # The server sends isPrivate as a boolean (ApiAddChatTag); str() turned that
        # into "True"/"False", which is neither the Java nor the JS shape.
        raw_is_private = dictionary.get(self.__KEY_ISPRIVATE)
        if raw_is_private is None:
            self.is_private = None
        elif isinstance(raw_is_private, bool):
            self.is_private = 1 if raw_is_private else 0
        else:
            self.is_private = Utils.to_long(raw_is_private)

    def to_json_obj(self):

        dictionary = {}

        if self.id is not None:
            dictionary[self.__KEY_ID] = self.id
        if self.name is not None:
            dictionary[self.__KEY_NAME] = self.name
        if self.description is not None:
            dictionary[self.__KEY_DESCRIPTION] = self.description
        if self.is_private is not None:
            dictionary[self.__KEY_ISPRIVATE] = self.is_private

        return json.dumps(dictionary), dictionary
