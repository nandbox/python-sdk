import json

from nandboxbots.outmessages.OutMessage import OutMessage


class DeleteWhiteListPatternsOutMessage(OutMessage):
    __KEY_PATTERN = "patterns"

    pattern = []

    def __init__(self):
        self.method = "removeWhitelistPatterns"

    def to_json_obj(self):
        _, dictionary = super(DeleteWhiteListPatternsOutMessage, self).to_json_obj()

        if self.pattern is not None:
            # Was dictionary[self.pattern], i.e. the value used as the key: a list
            # pattern raised TypeError and a string produced {"<pattern>": ...}.
            dictionary[self.__KEY_PATTERN] = self.pattern

        return json.dumps(dictionary), dictionary
    