import json

from nandboxbots.outmessages.OutMessage import OutMessage


class SetRecordOutMessage(OutMessage):
    __KEY_DOC_TYPE = "doc_type"
    __KEY_DOC_ID = "doc_id"
    __KEY_DOC = "doc"

    def __init__(self):
        self.method = "extensionSetDoc"

        self.doc = None
        self.table_name = None
        self.id = None

    def to_json_obj(self):
        _, obj = super(SetRecordOutMessage, self).to_json_obj()

        if self.table_name is not None:
            obj[self.__KEY_DOC_TYPE] = self.table_name

        if self.id is not None:
            obj[self.__KEY_DOC_ID] = self.id

        if self.doc is not None:
            obj[self.__KEY_DOC] = self.doc

        return json.dumps(obj), obj