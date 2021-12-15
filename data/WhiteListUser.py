import json


class WhiteListUser:
    KEY_SIGNUP_USER = "signup_user"
    KEY_TAGS = "tags"

    signup_user = None
    tags = []

    def __init__(self, dictionary):
        self.signup_user = str(dictionary[self.KEY_SIGNUP_USER]) if self.KEY_SIGNUP_USER in dictionary.keys() else None
        self.tags = dictionary[self.KEY_TAGS] if self.KEY_TAGS in dictionary.keys() else None

    def to_json_obj(self):

        dictionary = {}

        if self.signup_user is not None:
            dictionary[self.KEY_SIGNUP_USER] = self.signup_user
        if not self.tags == []:
            dictionary[self.KEY_TAGS] = self.tags

        return json.dumps(dictionary), dictionary
