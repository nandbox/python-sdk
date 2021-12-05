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
        chat_menu_callback_dict = dictionary[self.KEY_CHAT_MENU_CALL_BACK]

        from_user = User(dictionary[self.KEY_FROM])

        self.chat = Chat(dictionary[self.KEY_CHAT]) if dictionary[self.KEY_CHAT] is not None else None

        btn_query_result = ButtonQueryResult(dictionary[self.KEY_BUTTON_QUERY_RESULTS]) if dictionary[
                                                                                               self.KEY_BUTTON_QUERY_RESULTS] is not None else None

        self.method = str(dictionary[self.KEY_METHOD])
        self.menu_ref = str(dictionary[self.KEY_MENU_REF])
        self.from_ = from_user
        self.button_query_result = btn_query_result
        self.button_callback = str(dictionary[self.KEY_BUTTON_CALLBACK])
        self.next_menu = str(dictionary[self.KEY_NEXT_MENU])
        self.date = int(dictionary[self.KEY_DATE])

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
