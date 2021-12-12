import json

from outmessages.OutMessage import OutMessage


class DocumentOutMessage(OutMessage):
    KEY_DOCUMENT = "document"
    KEY_NAME = "name"
    KEY_SIZE = "size"

    document = None
    name = None
    size = None

    def __init__(self):
        self.method = "sendDocument"

    def to_json_obj(self):
        _, dictionary = super(DocumentOutMessage, self).to_json_obj()

        if self.document is not None:
            dictionary[self.KEY_DOCUMENT] = self.document
        if self.name is not None:
            dictionary[self.KEY_NAME] = self.name
        if self.size is not None:
            dictionary[self.KEY_SIZE] = self.size

        return json.dumps(dictionary), dictionary

