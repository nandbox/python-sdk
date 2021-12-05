import json


class SignupUser:
    KEY_ID = "id"
    KEY_SIGNUP_USER = "signup_user"

    id = None
    signup_user = None

    def __init__(self, dictionary):
        self.id = str(dictionary[self.KEY_ID])
        self.signup_user = str(dictionary[self.KEY_SIGNUP_USER])

    def to_json_obj(self):

        dictionary = {}

        if self.id is not None:
            dictionary[self.KEY_ID] = self.id
        if self.signup_user is not None:
            dictionary[self.KEY_SIGNUP_USER] = self.signup_user

        return json.dumps(dictionary), dictionary
