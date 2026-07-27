import json

from nandboxbots.outmessages.OutMessage import OutMessage


class SendUserNotificationOutMessage(OutMessage):
    """Sends a notification (SMS, Email or Push) to a single user."""

    SMS = "SMS"
    EMAIL = "Email"
    PUSH = "Push"

    __KEY_TYPE = "type"
    __KEY_TITLE = "title"
    __KEY_MESSAGE = "message"
    __KEY_ACCOUNT_ID = "account_id"

    type = None
    title = None
    message = None
    account_id = None

    def __init__(self):
        self.method = "sendUserNotification"

    def to_json_obj(self):
        _, dictionary = super(SendUserNotificationOutMessage, self).to_json_obj()

        # Mirrors the Java SDK: an unset type defaults to Push rather than being
        # omitted, because the server requires a notification type.
        dictionary[self.__KEY_TYPE] = self.type if self.type is not None else SendUserNotificationOutMessage.PUSH
        if self.title is not None:
            dictionary[self.__KEY_TITLE] = self.title
        if self.message is not None:
            dictionary[self.__KEY_MESSAGE] = self.message
        if self.account_id is not None:
            dictionary[self.__KEY_ACCOUNT_ID] = self.account_id

        return json.dumps(dictionary), dictionary
