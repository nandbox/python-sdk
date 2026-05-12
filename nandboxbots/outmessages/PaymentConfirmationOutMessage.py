import json

from nandboxbots.outmessages.OutMessage import OutMessage


class PaymentConfirmationOutMessage(OutMessage):
    __KEY_ORDER_ID = "order_id"
    __KEY_PAYLOAD = "payload"
    __KEY_SECRET = "secret"
    __KEY_CURRENCY = "currency"
    __KEY_TOTAL_AMOUNT = "total_amount"
    __KEY_ACCOUNT_ID = "account_id"
    __KEY_STATUS = "status"
    __KEY_DEBIT_AMOUNT_CENTS = "debit_amount_cents"

    def __init__(self):
        self.method = "paymentConfirmation"

        self.order_id = None
        self.payload = None
        self.secret = None
        self.currency = None
        self.total_amount = None
        self.account_id = None
        self.status = None
        self.debit_amount_cents = None

    def to_json_obj(self):
        _, obj = super(PaymentConfirmationOutMessage, self).to_json_obj()

        if self.order_id is not None:
            obj[self.__KEY_ORDER_ID] = self.order_id

        if self.payload is not None:
            obj[self.__KEY_PAYLOAD] = self.payload

        if self.secret is not None:
            obj[self.__KEY_SECRET] = self.secret

        if self.currency is not None:
            obj[self.__KEY_CURRENCY] = self.currency

        if self.total_amount is not None:
            obj[self.__KEY_TOTAL_AMOUNT] = self.total_amount

        if self.account_id is not None:
            obj[self.__KEY_ACCOUNT_ID] = self.account_id

        if self.status is not None:
            obj[self.__KEY_STATUS] = self.status

        if self.debit_amount_cents is not None:
            obj[self.__KEY_DEBIT_AMOUNT_CENTS] = self.debit_amount_cents

        return json.dumps(obj), obj