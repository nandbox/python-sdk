import json

from data.Chat import Chat
from data.User import User


class ChatMember:
    KEY_CHAT_MEMBER = "chatMember"
    KEY_USER = "user"
    KEY_CHAT = "chat"
    KEY_TYPE = "type"
    KEY_MEMBER_SINCE = "member_since"
    KEY_STATUS = "status"
    KEY_TAGS = "tags"
    KEY_ACCOUNT_TYPE = "account_type"
    KEY_MSISDN = "msisdn"

    user = None
    chat = None
    type = None
    member_since = None
    status = None
    tags = []
    account_type = None
    msisdn = None

    def __init__(self, dictionary):

        chat_member_dict = dictionary[self.KEY_CHAT_MEMBER]

        self.user = User(chat_member_dict[self.KEY_USER]) if chat_member_dict[self.KEY_USER] is not None else None
        self.chat = Chat(chat_member_dict[self.KEY_CHAT]) if chat_member_dict[self.KEY_CHAT] is not None else None
        self.type = str(chat_member_dict[self.KEY_TYPE])
        self.member_since = int(chat_member_dict[self.KEY_MEMBER_SINCE])
        self.status = str(chat_member_dict[self.KEY_STATUS])
        self.tags = chat_member_dict[self.KEY_TAGS]
        self.account_type = chat_member_dict[self.KEY_ACCOUNT_TYPE]
        self.msisdn = chat_member_dict[self.KEY_MSISDN]

    def to_json_obj(self):

        dictionary = {}

        if not self.tags == []:
            dictionary[self.KEY_TAGS] = self.tags
        if self.user is not None:
            _, user_dict = self.user.to_json_obj()
            dictionary[self.KEY_USER] = user_dict
        if self.chat is not None:
            _, chat_dict = self.chat.to_json_obj()
            dictionary[self.KEY_CHAT] = chat_dict
        if self.type is not None:
            dictionary[self.type] = self.type
        if self.member_since is not None:
            dictionary[self.KEY_MEMBER_SINCE] = self.member_since
        if self.status is not None:
            dictionary[self.KEY_STATUS] = self.status
        if self.account_type is not None:
            dictionary[self.KEY_ACCOUNT_TYPE] = self.account_type
        if self.msisdn is not None:
            dictionary[self.KEY_MSISDN] = self.msisdn

        return json.dumps(dictionary), dictionary
