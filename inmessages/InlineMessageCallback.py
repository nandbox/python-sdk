import json

from data.ButtonQueryResult import ButtonQueryResult
from data.Chat import Chat
from data.User import User


class InlineMessageCallback:
    KEY_INLINE_MESSAGE_CALLBACK = "inlineMessageCallback"
    KEY_MESSAGE_ID = "message_id"
    KEY_MENU_REF = "menu_ref"
    KEY_DATE = "date"
    KEY_FROM = "from"
    KEY_CHAT = "chat"
    KEY_REFERENCE = "reference"
    KEY_BUTTON_CALLBACK = "button_callback"
    KEY_BUTTON_QUERY_RESULTS = "button_query_result"

    message_id = None
    menu_ref = None
    date = None
    reference = None
    from_ = None
    chat = None
    button_callback = None
    button_query_result = None

    def __init__(self, dictionary):
        inline_message_dict = dictionary[self.KEY_INLINE_MESSAGE_CALLBACK] if self.KEY_INLINE_MESSAGE_CALLBACK in dictionary.keys() else {}

        from_user = User(inline_message_dict.get(self.KEY_FROM, {}))

        self.chat = Chat(inline_message_dict.get(self.KEY_CHAT, {}))

        btn_query_result = ButtonQueryResult(inline_message_dict.get(self.KEY_BUTTON_QUERY_RESULTS, {}))
        self.message_id = str(inline_message_dict[self.KEY_MESSAGE_ID]) if self.KEY_MESSAGE_ID in inline_message_dict.keys() else None
        self.menu_ref = str(inline_message_dict[self.KEY_MENU_REF]) if self.KEY_MENU_REF in inline_message_dict.keys() else None
        self.reference = str(inline_message_dict[self.KEY_REFERENCE]) if self.KEY_REFERENCE in inline_message_dict.keys() else None
        self.from_ = from_user
        self.button_query_result = btn_query_result
        self.button_callback = str(inline_message_dict[self.KEY_BUTTON_CALLBACK]) if self.KEY_BUTTON_CALLBACK in inline_message_dict.keys() else None
        self.date = int(inline_message_dict[self.KEY_DATE]) if self.KEY_DATE in inline_message_dict.keys() else None

    def to_json_obj(self):

        dictionary = {}

        if self.date is not None:
            dictionary[self.KEY_DATE] = self.date
        if self.from_ is not None:
            _, from_user_dict = self.from_.to_json_obj()
            dictionary[self.KEY_FROM] = from_user_dict
        if self.chat is not None:
            _, chat_dict = self.chat.to_json_obj()
            dictionary[self.KEY_CHAT] = chat_dict
        if self.message_id is not None:
            dictionary[self.KEY_MESSAGE_ID] = self.message_id
        if self.menu_ref is not None:
            dictionary[self.KEY_MENU_REF] = self.menu_ref
        if self.reference is not None:
            dictionary[self.KEY_REFERENCE] = self.reference
        if self.button_callback is not None:
            dictionary[self.KEY_BUTTON_CALLBACK] = self.button_callback
        if self.button_query_result is not None:
            _, btn_query_result_dict = self.button_query_result.to_json_obj()
            dictionary[self.KEY_BUTTON_QUERY_RESULTS] = btn_query_result_dict

        return json.dumps(dictionary), dictionary

