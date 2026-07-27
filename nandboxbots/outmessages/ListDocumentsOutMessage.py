import json

from nandboxbots.outmessages.OutMessage import OutMessage


class ListDocumentsOutMessage(OutMessage):
    """Lists documents in a collection, optionally filtered, sorted and paged.

    Replaces ListRecordsOutMessage, which could only fetch an entire collection in one unbounded
    response.

        msg = ListDocumentsOutMessage()
        msg.collection = "orders"
        msg.filter = {"status": "shipped", "total": {"$gte": 100}}
        msg.sort = {"created_at": -1}       # -1 descending, 1 ascending
        msg.page_size = 50
        msg.page_number = 0

    Operators: $eq $ne $gt $gte $lt $lte $in $nin $exists $contains $like.
    A bare value means equality.
    """

    __KEY_COLLECTION = "collection"
    __KEY_FILTER = "filter"
    __KEY_SORT = "sort"
    __KEY_PAGE_SIZE = "page_size"
    __KEY_PAGE_NUMBER = "page_number"

    collection = None
    filter = None
    sort = None
    #: Server default is 50 and the hard ceiling is 200; larger values are clamped.
    page_size = None
    #: Zero-based.
    page_number = None

    def __init__(self):
        self.method = "listDocuments"

    def to_json_obj(self):
        _, dictionary = super(ListDocumentsOutMessage, self).to_json_obj()

        if self.collection is not None:
            dictionary[self.__KEY_COLLECTION] = self.collection
        if self.filter is not None:
            dictionary[self.__KEY_FILTER] = self.filter
        if self.sort is not None:
            dictionary[self.__KEY_SORT] = self.sort
        if self.page_size is not None:
            dictionary[self.__KEY_PAGE_SIZE] = self.page_size
        if self.page_number is not None:
            dictionary[self.__KEY_PAGE_NUMBER] = self.page_number

        return json.dumps(dictionary), dictionary
