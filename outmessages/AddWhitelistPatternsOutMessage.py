import json

from outmessages.OutMessage import OutMessage


class AddWhitelistPatternsOutMessage(OutMessage):
    KEY_DATA = "data"

    data = []

    def __init__(self):
        self.method = "addWhitelistPatterns"

    def to_json_obj(self):
        _, dictionary = super(AddWhitelistPatternsOutMessage, self).to_json_obj()

        if self.data is not None:
            dictionary[self.KEY_DATA] = self.data
            
        return json.dumps(dictionary), dictionary
    