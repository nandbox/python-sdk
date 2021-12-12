import json

from outmessages.OutMessage import OutMessage


class UpdateOutMessage(OutMessage):
    KEY_MESSAGE_ID = "message_id"
    KEY_TEXT = "text"

    message_id = None
    text = None

    def __init__(self):
        self.method = "updateMessage"

    def to_json_obj(self):
        _, dictionary = super(UpdateOutMessage, self).to_json_obj()

        if self.message_id is not None:
            dictionary[self.KEY_MESSAGE_ID] = self.message_id
        if self.text is not None:
            dictionary[self.KEY_TEXT] = self.text
        if self.caption is not None:
            dictionary[self.KEY_CAPTION] = self.caption
        if self.to_user_id is not None:
            dictionary[self.KEY_TO_USER_ID] = self.to_user_id
        if self.chat_id is not None:
            dictionary[self.KEY_CHAT_ID] = self.chat_id

        return json.dumps(dictionary), dictionary
