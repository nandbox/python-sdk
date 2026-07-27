import json


class WebhookBody:
    """Inbound `WebhookEvent` payload.

    The envelope fields (ref, app_id, method) are lifted out and everything else
    is exposed as `body`.
    """

    __KEY_REF = "ref"
    __KEY_APP_ID = "app_id"
    __KEY_METHOD = "method"

    def __init__(self, dictionary=None):
        # Work on a shallow copy so the caller's dict is not mutated and `body`
        # does not alias it.
        payload = dict(dictionary or {})

        self.ref = str(payload.pop(self.__KEY_REF)) if payload.get(self.__KEY_REF) is not None else None
        self.app_id = str(payload.pop(self.__KEY_APP_ID)) if payload.get(self.__KEY_APP_ID) is not None else None
        self.method = str(payload.pop(self.__KEY_METHOD)) if payload.get(self.__KEY_METHOD) is not None else None

        # Drop the keys even when their value was null, so they never leak into body.
        payload.pop(self.__KEY_REF, None)
        payload.pop(self.__KEY_APP_ID, None)
        payload.pop(self.__KEY_METHOD, None)

        self.body = payload

    def to_json_obj(self):
        dictionary = dict(self.body)
        if self.ref is not None:
            dictionary[self.__KEY_REF] = self.ref
        if self.app_id is not None:
            dictionary[self.__KEY_APP_ID] = self.app_id
        if self.method is not None:
            dictionary[self.__KEY_METHOD] = self.method
        return json.dumps(dictionary), dictionary
