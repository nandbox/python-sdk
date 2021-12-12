import json

from outmessages.OutMessage import OutMessage


class PhotoOutMessage(OutMessage):
    KEY_PHOTO = "photo"

    photo = None

    def __init__(self):
        self.method = "sendPhoto"

    def to_json_obj(self):
        _, dictionary = super(PhotoOutMessage, self).to_json_obj()

        if self.photo is not None:
            dictionary[self.KEY_PHOTO] = self.photo

        return json.dumps(dictionary), dictionary
