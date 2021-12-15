import json

from data.ButtonQueryResult import ButtonQueryResult
from data.Chat import Chat
from data.User import User


class ChatMenuCallback:
    KEY_CHAT_MENU_CALL_BACK = "chatMenuCallback"
    KEY_DATE = "date"
    KEY_NEXT_MENU = "next_menu"
    KEY_METHOD = "method"
    KEY_BUTTON_CALLBACK = "button_callback"
    KEY_BUTTON_QUERY_RESULTS = "button_query_result"
    KEY_CHAT = "chat"
    KEY_FROM = "from"
    KEY_MENU_REF = "menu_ref"

    date = None
    next_menu = None
    method = None
    button_callback = None
    button_query_result = None
    chat = None
    from_ = None
    menu_ref = None

    def __init__(self, dictionary):
        chat_menu_callback_dict = dictionary[self.KEY_CHAT_MENU_CALL_BACK] if self.KEY_CHAT_MENU_CALL_BACK in dictionary.keys() else {}

        from_user = User(chat_menu_callback_dict.get(self.KEY_FROM, {}))

        self.chat = Chat(chat_menu_callback_dict.get(self.KEY_CHAT, {}))

        btn_query_result = ButtonQueryResult(chat_menu_callback_dict.get(self.KEY_BUTTON_QUERY_RESULTS, {}))

        self.method = str(chat_menu_callback_dict[self.KEY_METHOD]) if self.KEY_METHOD in chat_menu_callback_dict.keys() else None
        self.menu_ref = str(chat_menu_callback_dict[self.KEY_MENU_REF]) if self.KEY_MENU_REF in chat_menu_callback_dict.keys() else None
        self.from_ = from_user
        self.button_query_result = btn_query_result
        self.button_callback = str(chat_menu_callback_dict[self.KEY_BUTTON_CALLBACK]) if self.KEY_BUTTON_CALLBACK in chat_menu_callback_dict.keys() else None
        self.next_menu = str(chat_menu_callback_dict[self.KEY_NEXT_MENU]) if self.KEY_NEXT_MENU in chat_menu_callback_dict.keys() else None
        self.date = int(chat_menu_callback_dict[self.KEY_DATE]) if self.KEY_DATE in chat_menu_callback_dict.keys() else None

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
        if self.method is not None:
            dictionary[self.KEY_METHOD] = self.method
        if self.menu_ref is not None:
            dictionary[self.KEY_MENU_REF] = self.menu_ref
        if self.button_callback is not None:
            dictionary[self.KEY_BUTTON_CALLBACK] = self.button_callback
        if self.button_query_result is not None:
            _, btn_query_result_dict = self.button_query_result.to_json_obj()
            dictionary[self.KEY_BUTTON_QUERY_RESULTS] = btn_query_result_dict
        if self.next_menu is not None:
            dictionary[self.KEY_NEXT_MENU] = self.next_menu

        return json.dumps(dictionary), dictionary
