def _as_string(value):
    return None if value is None else str(value)


class EventMessage:
    """A change on an event the account is subscribed to.

    The payload is deliberately left as a raw dict. The server decides per event which keys
    survive its filter, and that set changes without a client release - so modelling the payload
    as fixed attributes would silently drop whatever was added and break on whatever was removed.
    Read what you need out of ``body`` and tolerate a missing key.

        def on_event_message(self, event_message):
            if event_message.event == "product":
                product_id = event_message.body.get("id")
                price = event_message.get("price")      # may be absent

    ``body`` is the whole message, so method, event and app_id are in there too alongside the
    payload keys.
    """

    __KEY_METHOD = "method"
    __KEY_EVENT = "event"
    __KEY_APP_ID = "app_id"

    def __init__(self, dictionary):
        #: The message as received. Its keys vary by event and by the server side filter.
        self.body = dictionary if isinstance(dictionary, dict) else {}

        self.method = _as_string(self.body.get(self.__KEY_METHOD))

        #: Which event fired: product, chat, chatMember, content or order.
        self.event = _as_string(self.body.get(self.__KEY_EVENT))

        self.app_id = _as_string(self.body.get(self.__KEY_APP_ID))

    def get(self, key, default=None):
        """Convenience for a single key, ``default`` when the filter did not include it."""
        return self.body.get(key, default)
