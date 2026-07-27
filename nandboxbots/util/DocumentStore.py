from nandboxbots.outmessages.SetDocumentOutMessage import SetDocumentOutMessage
from nandboxbots.outmessages.GetDocumentOutMessage import GetDocumentOutMessage
from nandboxbots.outmessages.ListDocumentsOutMessage import ListDocumentsOutMessage
from nandboxbots.outmessages.DeleteDocumentOutMessage import DeleteDocumentOutMessage


class DocumentStore:
    """Per-bot storage for JSON documents, grouped into collections.

    Replaces DatabaseService. Two things changed beyond the naming:

    - Messages are serialised before sending. DatabaseService called api.send(out_message), but
      send expects the JSON string produced by to_json_obj, so it was passing an object. Nothing
      it sent was ever a valid frame.
    - The argument order is consistent: every method takes (api, collection, document_id, ...).
      The old class took set(api, obj, table_name, doc_id) but get(api, doc_id, table_name), so
      the two middle arguments swapped between calls with nothing to catch it.

    Every method replies through callback.on_document_response.
    """

    __instance = None

    @staticmethod
    def get_instance():
        if DocumentStore.__instance is None:
            DocumentStore.__instance = DocumentStore()

        return DocumentStore.__instance

    def set_document(self, api, collection, document_id, document, reference=None):
        """Creates the document, or replaces it entirely if the id already exists.

        There is no partial update: whatever is passed becomes the stored document.
        """
        out_message = SetDocumentOutMessage()
        out_message.collection = collection
        out_message.document_id = document_id
        out_message.document = document
        out_message.reference = reference

        obj, _ = out_message.to_json_obj()
        api.send(obj)

    def get_document(self, api, collection, document_id, reference=None):
        """Fetches one document. The reply carries a None document when the id does not exist."""
        out_message = GetDocumentOutMessage()
        out_message.collection = collection
        out_message.document_id = document_id
        out_message.reference = reference

        obj, _ = out_message.to_json_obj()
        api.send(obj)

    def delete_document(self, api, collection, document_id, reference=None):
        """Deletes one document. The reply's ack is 0 when nothing matched."""
        out_message = DeleteDocumentOutMessage()
        out_message.collection = collection
        out_message.document_id = document_id
        out_message.reference = reference

        obj, _ = out_message.to_json_obj()
        api.send(obj)

    def list_documents(self, api, collection, reference=None, filter=None, sort=None,
                       page_size=None, page_number=None):
        """Lists documents, optionally filtered, sorted and paged.

            store.list_documents(api, "orders", reference)
            store.list_documents(
                api, "orders", reference,
                filter={"status": "shipped", "total": {"$gte": 100}},
                sort={"created_at": -1},
                page_size=50,
                page_number=0,
            )

        Operators: $eq $ne $gt $gte $lt $lte $in $nin $exists $contains $like. A bare value
        means equality. Filtering scans the collection, so keep pages small.
        """
        out_message = ListDocumentsOutMessage()
        out_message.collection = collection
        out_message.reference = reference
        out_message.filter = filter
        out_message.sort = sort
        out_message.page_size = page_size
        out_message.page_number = page_number

        obj, _ = out_message.to_json_obj()
        api.send(obj)
