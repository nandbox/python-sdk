import json

from nandboxbots.outmessages.OutMessage import OutMessage


class ListEventSubscriptionsOutMessage(OutMessage):
    """Lists the events an account is currently subscribed to in an app.

    Lets a client reconcile after a reconnect instead of blindly re-subscribing.

        msg = ListEventSubscriptionsOutMessage()
        msg.app_id = "1234"

    The reply is a listEventSubscriptionsResponse, delivered to Callback.on_event_response with
    the events in ``response.events``.
    """

    __KEY_ACCOUNT_ID = "account_id"

    #: Leave unset to list your own subscriptions. Another account requires app admin.
    account_id = None

    def __init__(self):
        self.method = "listEventSubscriptions"

    def to_json_obj(self):
        _, dictionary = super(ListEventSubscriptionsOutMessage, self).to_json_obj()

        if self.account_id is not None:
            dictionary[self.__KEY_ACCOUNT_ID] = self.account_id

        return json.dumps(dictionary), dictionary
