import json

from nandboxbots.outmessages.OutMessage import OutMessage


class DeleteDocumentOutMessage(OutMessage):
    """Deletes one document by its id.

    Replaces DeleteRecordOutMessage.
    """

    __KEY_COLLECTION = "collection"
    __KEY_DOCUMENT_ID = "document_id"

    collection = None
    document_id = None

    def __init__(self):
        self.method = "deleteDocument"

    def to_json_obj(self):
        _, dictionary = super(DeleteDocumentOutMessage, self).to_json_obj()

        if self.collection is not None:
            dictionary[self.__KEY_COLLECTION] = self.collection
        if self.document_id is not None:
            dictionary[self.__KEY_DOCUMENT_ID] = self.document_id

        return json.dumps(dictionary), dictionary
