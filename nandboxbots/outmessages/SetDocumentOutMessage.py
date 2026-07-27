import json

from nandboxbots.outmessages.OutMessage import OutMessage


class SetDocumentOutMessage(OutMessage):
    """Stores a document in a collection, creating it or replacing it in place.

    Replaces SetRecordOutMessage. The "table" vocabulary it used implied columns and a schema
    that the document store does not have.
    """

    __KEY_COLLECTION = "collection"
    __KEY_DOCUMENT_ID = "document_id"
    __KEY_DOCUMENT = "document"

    collection = None
    document_id = None
    document = None

    def __init__(self):
        self.method = "setDocument"

    def to_json_obj(self):
        _, dictionary = super(SetDocumentOutMessage, self).to_json_obj()

        if self.collection is not None:
            dictionary[self.__KEY_COLLECTION] = self.collection
        if self.document_id is not None:
            dictionary[self.__KEY_DOCUMENT_ID] = self.document_id
        if self.document is not None:
            dictionary[self.__KEY_DOCUMENT] = self.document

        return json.dumps(dictionary), dictionary
