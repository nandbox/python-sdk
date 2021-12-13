import json

from outmessages.OutMessage import OutMessage


class InlineSearchAnswer(OutMessage):
    KEY_RESULTS = "results"
    KEY_SEARCH_ID = "search_id"
    KEY_NEXT_OFFSET = "next_offset"

    results = []
    search_id = None
    next_offset = None

    def __init__(self):
        self.method = "inlineSearchAnswer"

    def to_json_obj(self):
        _, dictionary = super(InlineSearchAnswer, self).to_json_obj()

        if self.results is not None:
            dictionary[self.KEY_RESULTS] = self.results
        if self.search_id is not None:
            dictionary[self.KEY_SEARCH_ID] = self.search_id
        if self.next_offset is not None:
            dictionary[self.KEY_NEXT_OFFSET] = self.next_offset

        return json.dumps(dictionary), dictionary
