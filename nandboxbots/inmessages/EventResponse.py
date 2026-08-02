from nandboxbots.util import Utils


def _as_string(value):
    return None if value is None else str(value)


class EventResponse:
    """Reply to subscribeToEvent, unsubscribeFromEvent and listEventSubscriptions.

    ``ack`` is the only success test: False means nothing changed and ``error`` says why. Common
    errors are 400 (missing app id, or an event the server does not publish), 160017 (privilege
    missing for that event), 160024 (the account is not a member of the app) and 160015 (unknown
    app).

    For a subscribe or unsubscribe reply, ``events`` echoes what the request asked for. For a
    list reply, it is the account's current subscriptions.
    """

    __KEY_METHOD = "method"
    __KEY_EVENT = "event"
    __KEY_EVENTS = "events"
    __KEY_APP_ID = "app_id"
    __KEY_ACCOUNT_ID = "account_id"
    __KEY_ACK = "ack"
    __KEY_ERROR = "error"
    __KEY_REFERENCE = "reference"
    __KEY_REF = "ref"

    def __init__(self, dictionary):
        #: eventResponse or listEventSubscriptionsResponse.
        self.method = _as_string(dictionary.get(self.__KEY_METHOD))

        #: Always a list; empty when a list reply found no subscriptions.
        events = dictionary.get(self.__KEY_EVENTS)
        self.events = [str(item) for item in events if item is not None] if isinstance(events, list) else []

        # single event requests also echo "event"; keep the list authoritative either way
        single = _as_string(dictionary.get(self.__KEY_EVENT))
        if single is not None and single not in self.events:
            self.events.append(single)

        #: The first event, for the common single event request. None when there are none.
        self.event = self.events[0] if self.events else None

        self.app_id = _as_string(dictionary.get(self.__KEY_APP_ID))

        #: The account the subscription applies to, which is the caller unless one was set.
        self.account_id = _as_string(dictionary.get(self.__KEY_ACCOUNT_ID))

        #: True when the request took effect. False means look at ``error``.
        ack = dictionary.get(self.__KEY_ACK)
        self.ack = None if ack is None else Utils.to_bool(ack)

        #: Server error code, set only when ack is False.
        error = dictionary.get(self.__KEY_ERROR)
        self.error = None if error is None else Utils.to_long(error)

        reference = dictionary.get(self.__KEY_REFERENCE)
        if reference is None:
            reference = dictionary.get(self.__KEY_REF)
        self.reference = _as_string(reference)
