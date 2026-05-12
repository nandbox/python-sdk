import json

from nandboxbots.outmessages.OutMessage import OutMessage


class ListRecordsOutMessage(OutMessage):
    __KEY_DOC_TYPE = "doc_type"

    def __init__(self):
        self.method = "extensionListDoc"

        self.table_name = None

    def to_json_obj(self):
        _, obj = super(ListRecordsOutMessage, self).to_json_obj()

        if self.table_name is not None:
            obj[self.__KEY_DOC_TYPE] = self.table_name

        return json.dumps(obj), obj