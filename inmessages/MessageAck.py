import json


class MessageAck:
    KEY_ACK = "ack"
    KEY_MESSAGE_ID = "message_id"
    KEY_DATE = "date"
    KEY_REFERENCE = "reference"

    message_id = None
    date = None
    reference = None

    def __init__(self, dictionary):

        ack_dict = dictionary[self.KEY_ACK]

        self.message_id = str(ack_dict[self.KEY_MESSAGE_ID])
        self.reference = str(ack_dict[self.KEY_REFERENCE])
        self.date = int(ack_dict[self.KEY_DATE])

    def to_json_obj(self):

        dictionary = {}

        if self.date is not None:
            dictionary[self.KEY_DATE] = self.date
        if self.message_id is not None:
            dictionary[self.KEY_MESSAGE_ID] = self.message_id
        if self.reference is not None:
            dictionary[self.KEY_REFERENCE] = self.reference

        return json.dumps(dictionary), dictionary
