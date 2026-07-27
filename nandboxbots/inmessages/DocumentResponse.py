from nandboxbots.util import Utils


def _as_string(value):
    return None if value is None else str(value)


class DocumentEntry:
    """One entry of a list reply: the document and the id it is stored under."""

    def __init__(self, document_id, document):
        self.document_id = document_id
        self.document = document

    def __repr__(self):
        return "DocumentEntry(document_id=%r, document=%r)" % (self.document_id, self.document)


class DocumentResponse:
    """Reply to any of the document store methods.

    Replaces ExtensionDocResponse. Two things changed beyond the naming:

    - The list reply used to be parsed by re-parsing the array's string form, so entries came
      back as strings rather than dicts. The server now sends real objects and this class reads
      them directly.
    - List replies carry the document id alongside each payload, so a caller no longer has to
      store the id inside the document to know which one it is looking at.
    """

    __KEY_COLLECTION = "collection"
    __KEY_DOCUMENT_ID = "document_id"
    __KEY_DOCUMENT = "document"
    __KEY_DOCUMENTS = "documents"
    __KEY_REFERENCE = "reference"
    __KEY_REF = "ref"
    __KEY_APP_ID = "app_id"
    __KEY_METHOD = "method"
    __KEY_ACK = "ack"
    __KEY_PAGE_NUMBER = "page_number"
    __KEY_EOP = "eop"

    def __init__(self, dictionary):
        #: Collection the document or documents belong to.
        self.collection = _as_string(dictionary.get(self.__KEY_COLLECTION))

        #: Set for get, set and delete replies; None for a list reply.
        self.document_id = _as_string(dictionary.get(self.__KEY_DOCUMENT_ID))

        #: The document, for get and set replies. None when the id was not found.
        document = dictionary.get(self.__KEY_DOCUMENT)
        self.document = document if isinstance(document, dict) else None

        #: One page of DocumentEntry, for a list reply. None for the single-document methods.
        documents = dictionary.get(self.__KEY_DOCUMENTS)
        if isinstance(documents, list):
            self.documents = []
            for entry in documents:
                if not isinstance(entry, dict):
                    continue
                payload = entry.get(self.__KEY_DOCUMENT)
                self.documents.append(DocumentEntry(
                    _as_string(entry.get(self.__KEY_DOCUMENT_ID)),
                    payload if isinstance(payload, dict) else None))
        else:
            self.documents = None

        reference = dictionary.get(self.__KEY_REFERENCE)
        if reference is None:
            reference = dictionary.get(self.__KEY_REF)
        self.reference = _as_string(reference)

        self.app_id = _as_string(dictionary.get(self.__KEY_APP_ID))
        self.method = _as_string(dictionary.get(self.__KEY_METHOD))

        #: Rows affected, for set and delete. Zero from a delete means nothing matched.
        ack = dictionary.get(self.__KEY_ACK)
        self.ack = None if ack is None else Utils.to_long(ack)

        #: Page this reply represents, for a list reply.
        page_number = dictionary.get(self.__KEY_PAGE_NUMBER)
        self.page_number = None if page_number is None else Utils.to_long(page_number)

        #: True when there are no further pages.
        eop = dictionary.get(self.__KEY_EOP)
        self.eop = None if eop is None else Utils.to_bool(eop)
