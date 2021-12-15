import json

from data.Chat import Chat
from data.User import User


class ChatAdministrators:
    KEY_CHAT_ADMINISTRATORS = "chatAdministrators"
    KEY_ADMINISTRATORS = "administrators"
    KEY_CHAT = "chat"

    administrators = []
    chat = None

    def __init__(self, dictionary):

        chat_administrators_dict = dictionary[self.KEY_CHAT_ADMINISTRATORS] if self.KEY_CHAT_ADMINISTRATORS in dictionary.keys() else {}

        self.chat = Chat(chat_administrators_dict.get(self.KEY_CHAT, {}))

        admin_arr_obj = chat_administrators_dict[self.KEY_ADMINISTRATORS] if self.KEY_ADMINISTRATORS in chat_administrators_dict.keys() else None
        if admin_arr_obj is not None:
            length = len(admin_arr_obj)
            admin = [User({})] * length
            for i in range(length):
                admin[i] = User(admin_arr_obj[i])

            self.administrators = admin

    def to_json_obj(self):

        dictionary = {}

        if self.administrators is not None:
            admins_arr = []
            for i in range(len(self.administrators)):
                admins_arr.append(self.administrators[i].to_json_obj())

            dictionary[self.KEY_ADMINISTRATORS] = admins_arr

        if self.chat is not None:
            _, chat_dict = self.chat.to_json_obj()
            dictionary[self.KEY_CHAT] = chat_dict

        return json.dumps(dictionary), dictionary
