import json

from data.Chat import Chat
from data.SignupUser import SignupUser


class WhiteList:
    KEY_WHITELIST = "whitelist"
    KEY_EOP = "eop"
    KEY_USERS = "users"
    KEY_CHAT = "chat"

    eop = None
    chat = None
    users = []

    def __init__(self, dictionary):
        whitelist_dict = dictionary[self.KEY_WHITELIST] if self.KEY_WHITELIST in dictionary.keys() else {}

        self.eop = str(whitelist_dict[self.KEY_EOP]) if self.KEY_EOP in whitelist_dict.keys() else None
        self.chat = Chat(whitelist_dict.get(self.KEY_CHAT, {}))

        users_arr_obj = whitelist_dict[self.KEY_USERS] if self.KEY_USERS in whitelist_dict.keys() else []
        self.users = [SignupUser({})] * len(users_arr_obj)
        for i in range(len(users_arr_obj)):
            self.users[i] = SignupUser(users_arr_obj[i])

    def to_json_obj(self):

        dictionary = {}

        if self.users is not None:
            users_arr = []
            for i in range(len(self.users)):
                users_arr.append(self.users[i].to_json_obj())

            dictionary[self.KEY_USERS] = users_arr

        if self.chat is not None:
            _, chat_dict = self.chat.to_json_obj()
            dictionary[self.KEY_CHAT] = chat_dict

        if self.eop is not None:
            dictionary[self.KEY_EOP] = self.eop

        return json.dumps(dictionary), dictionary
