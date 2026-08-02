from nandboxbots.outmessages.EventSubscriptionOutMessage import EventSubscriptionOutMessage


class UnsubscribeFromEventOutMessage(EventSubscriptionOutMessage):
    """Stops delivery of one or more events to an account.

        msg = UnsubscribeFromEventOutMessage()
        msg.app_id = "1234"
        msg.event = "product"

    The reply is an eventResponse. Unsubscribing from something you are not subscribed to still
    acks. Unsubscribing yourself never requires a privilege.
    """

    def __init__(self):
        self.method = "unsubscribeFromEvent"
