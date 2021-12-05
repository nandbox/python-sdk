import json

from data.Chat import Chat
from data.SignupUser import SignupUser


class BlackList:
    KEY_BLACKLIST = "blacklist"
    KEY_EOP = "eop"
    KEY_USERS = "users"
    KEY_CHAT = "chat"

    eop = None
    chat = None
    users = []

    def __init__(self, dictionary):
        blacklist_dict = dictionary[self.KEY_BLACKLIST]

        self.eop = str(blacklist_dict[self.KEY_EOP])
        self.chat = Chat(blacklist_dict[self.KEY_CHAT]) if blacklist_dict[self.KEY_CHAT] is not None else None

        users_arr_obj = blacklist_dict[self.KEY_USERS]
        self.users = [SignupUser()] * len(users_arr_obj)
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
