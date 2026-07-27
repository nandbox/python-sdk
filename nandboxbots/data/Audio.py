import json


class Audio:
    __KEY_ID = "id"
    __KEY_TITLE = "title"
    __KEY_PERFORMER = "performer"
    __KEY_SIZE = "size"
    __KEY_DURATION = "duration"

    id = None
    title = None
    performer = None
    size = None
    duration = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.__KEY_ID]) if dictionary.get(self.__KEY_ID) is not None else None
        self.title = str(dictionary[self.__KEY_TITLE]) if dictionary.get(self.__KEY_TITLE) is not None else None
        self.performer = str(dictionary[self.__KEY_PERFORMER]) if dictionary.get(self.__KEY_PERFORMER) is not None else None
        self.size = int(dictionary[self.__KEY_SIZE]) if dictionary.get(self.__KEY_SIZE) is not None else None
        self.duration = int(dictionary[self.__KEY_DURATION]) if dictionary.get(self.__KEY_DURATION) is not None else None

    def to_json_obj(self):

        dictionary = {}

        if self.id is not None:
            dictionary[self.__KEY_ID] = self.id
        if self.title is not None:
            dictionary[self.__KEY_TITLE] = self.title
        if self.performer is not None:
            dictionary[self.__KEY_PERFORMER] = self.performer
        if self.size is not None:
            dictionary[self.__KEY_SIZE] = self.size
        if self.duration is not None:
            dictionary[self.__KEY_DURATION] = self.duration

        return json.dumps(dictionary), dictionary
