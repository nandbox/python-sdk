import json

from outmessages.OutMessage import OutMessage


class DeleteBlackListPatternsOutMessage(OutMessage):
    KEY_PATTERN = "pattern"

    pattern = []

    def to_json_obj(self):
        _, dictionary = super(DeleteBlackListPatternsOutMessage, self).to_json_obj()

        if self.pattern is not None:
            dictionary[self.KEY_PATTERN] = self.pattern

        return json.dumps(dictionary), dictionary
    