import json

from outmessages.OutMessage import OutMessage


class AddWhiteListOutMessage(OutMessage):
    KEY_USERS = "users"

    white_list_user = []

    def __init__(self):
        self.method = "addWhitelist"

    def to_json_obj(self):
        _, dictionary = super(AddWhiteListOutMessage, self).to_json_obj()

        if self.white_list_user is not None:
            dictionary[self.KEY_USERS] = self.white_list_user

        return json.dumps(dictionary), dictionary

