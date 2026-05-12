import json


class PaymentRequest:
    __KEY_ORDER_ID = "order_id"
    __KEY_MERCHANT_NAME = "merchant_name"
    __KEY_AMOUNT = "amount"
    __KEY_CURRENCY = "currency"
    __KEY_PAYLOAD = "payload"
    __KEY_ACCOUNT_ID = "account_id"
    __KEY_SECRET = "secret"
    __KEY_APP_ID = "app_id"
    __KEY_PROVIDER_ID = "provider_id"
    __KEY_CONFIG = "config"
    __KEY_DEBIT_AMOUNT_CENTS = "debit_amount_cents"

    def __init__(self, obj):
        print("PaymentRequest JSON:", json.dumps(obj))

        self.order_id = None
        self.merchant_name = None
        self.amount = 0
        self.currency = None
        self.payload = None
        self.account_id = 0
        self.secret = None
        self.app_id = None
        self.config = None
        self.provider_id = None
        self.debit_amount_cents = 0

        if self.__KEY_ORDER_ID in obj:
            self.order_id = obj.get(self.__KEY_ORDER_ID)

        if self.__KEY_MERCHANT_NAME in obj:
            self.merchant_name = obj.get(self.__KEY_MERCHANT_NAME)

        if self.__KEY_AMOUNT in obj:
            self.amount = float(obj.get(self.__KEY_AMOUNT))

        if self.__KEY_CURRENCY in obj:
            self.currency = obj.get(self.__KEY_CURRENCY)

        if self.__KEY_PAYLOAD in obj:
            self.payload = obj.get(self.__KEY_PAYLOAD)

        if self.__KEY_ACCOUNT_ID in obj:
            self.account_id = int(obj.get(self.__KEY_ACCOUNT_ID))

        if self.__KEY_SECRET in obj:
            self.secret = obj.get(self.__KEY_SECRET)

        if self.__KEY_APP_ID in obj:
            self.app_id = str(obj.get(self.__KEY_APP_ID))

        if self.__KEY_PROVIDER_ID in obj:
            self.provider_id = str(obj.get(self.__KEY_PROVIDER_ID))

        if self.__KEY_CONFIG in obj:
            self.config = obj.get(self.__KEY_CONFIG)

        if self.__KEY_DEBIT_AMOUNT_CENTS in obj:
            self.debit_amount_cents = int(obj.get(self.__KEY_DEBIT_AMOUNT_CENTS))

    def to_json(self):
        obj = {}

        obj[self.__KEY_ORDER_ID] = self.order_id
        obj[self.__KEY_MERCHANT_NAME] = self.merchant_name
        obj[self.__KEY_AMOUNT] = self.amount
        obj[self.__KEY_CURRENCY] = self.currency
        obj[self.__KEY_PAYLOAD] = self.payload

        return obj

    def to_json_string(self):
        return json.dumps(self.to_json())