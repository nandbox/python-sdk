import json

from nandboxbots.outmessages.OutMessage import OutMessage


class UpdateOutMessage(OutMessage):
    __KEY_MESSAGE_ID = "message_id"
    __KEY_TEXT = "text"

    message_id = None
    text = None

    def __init__(self):
        self.method = "updateMessage"

    def to_json_obj(self):
        _, dictionary = super(UpdateOutMessage, self).to_json_obj()

        if self.message_id is not None:
            dictionary[self.__KEY_MESSAGE_ID] = self.message_id
        if self.text is not None:
            dictionary[self.__KEY_TEXT] = self.text
        # caption, to_user_id and chat_id are already emitted by OutMessage. The
        # explicit copies here referenced self.__KEY_* from this subclass, which
        # name-mangles to _UpdateOutMessage__KEY_* and does not exist, so every
        # update_* call raised AttributeError.

        return json.dumps(dictionary), dictionary
