import json

from nandboxbots.outmessages.OutMessage import OutMessage


class EventSubscriptionOutMessage(OutMessage):
    """Shared body of SubscribeToEventOutMessage and UnsubscribeFromEventOutMessage.

    Both carry the same fields and differ only in method.

    An event is a stream of app activity - product, chat, chatMember, content, order - that the
    server pushes as an eventMessage to every subscribed account.

    Set either ``event`` for the single case or ``events`` for several. ``account_id`` acts on
    another account and requires the caller to be an admin of the app; leave it unset to act on
    yourself.
    """

    __KEY_EVENT = "event"
    __KEY_EVENTS = "events"
    __KEY_ACCOUNT_ID = "account_id"

    event = None
    events = None
    account_id = None

    def to_json_obj(self):
        _, dictionary = super(EventSubscriptionOutMessage, self).to_json_obj()

        if self.events:
            dictionary[self.__KEY_EVENTS] = list(self.events)
        if self.event is not None:
            dictionary[self.__KEY_EVENT] = self.event
        if self.account_id is not None:
            dictionary[self.__KEY_ACCOUNT_ID] = self.account_id

        return json.dumps(dictionary), dictionary
