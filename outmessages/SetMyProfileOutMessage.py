import json

from outmessages.OutMessage import OutMessage


class SetMyProfileOutMessage(OutMessage):
    KEY_USER = "user"

    user = None

    def __init__(self):
        self.method = "setMyProfile"

    def to_json_obj(self):
        _, dictionary = super(SetMyProfileOutMessage, self).to_json_obj()

        if self.user is not None:
            dictionary[self.KEY_USER] = self.user

        return json.dumps(dictionary), dictionary
    
