import json


class Data:
    __KEY_PATTERN = "pattern"
    __KEY_EXAMPLE = "example"
    __KEY_ID = "id"
    __KEY_TAGS = "tags"


    pattern = None
    example = None
    id = None
    # ApiAddWhitelistPatterns reads "tags" off each pattern, but this class never
    # carried the field, so tags could not be assigned through the SDK.
    tags = None
    def __init__(self, dictionary=None):
        if dictionary is None or dictionary == {}:
            return
        self.pattern = str(dictionary[self.__KEY_PATTERN]) if dictionary.get(self.__KEY_PATTERN) is not None else None
        self.example = str(dictionary[self.__KEY_EXAMPLE]) if dictionary.get(self.__KEY_EXAMPLE) is not None else None
        self.id = str(dictionary[self.__KEY_ID]) if dictionary.get(self.__KEY_ID) is not None else None
        self.tags = dictionary.get(self.__KEY_TAGS)

    def to_dict(self):
        # Previously emitted every key including the unset ones, so a create call
        # went out carrying "id": null and "example": null.
        _, dictionary = self.to_json_obj()
        return dictionary

    def to_json_obj(self):

        dictionary = {}

        if self.pattern is not None:
            dictionary[self.__KEY_PATTERN] = self.pattern
        if self.example is not None:
            dictionary[self.__KEY_EXAMPLE] = self.example
        if self.id is not None:
            dictionary[self.__KEY_ID] = self.id
        if self.tags is not None:
            dictionary[self.__KEY_TAGS] = self.tags

        return json.dumps(dictionary), dictionary
