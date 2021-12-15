import json

from NandboxClient import NandboxClient
from nandbox import Nandbox

CONFIG_FILE = "../config.json"

f = open(CONFIG_FILE)
config = json.load(f)
f.close()

client = NandboxClient.get(config)

nandbox = Nandbox()

napi = nandbox.Api()

CYELLOW = '\033[93m'
CEND = '\033[0m'

def handle_incoming_text_msg(msg):
    pass


class nCallBack(nandbox.Callback):
    def on_connect(self, api):
        global napi
        napi = api
        print("Connected")

    def on_close(self):
        print("Closed")

    def on_error(self):
        print("Error")

    def on_receive(self, incoming_msg):
        print("=========>> " + incoming_msg.type + " Message Received =========>>")
        print("incoming_msg.message_id : " + incoming_msg.message_id)
        print("incoming_msg.date : " + incoming_msg.date)
        print("incoming_msg.reference : " + incoming_msg.reference)
        print("incoming_msg.caption: " + incoming_msg.caption)
        if incoming_msg.sent_to() is not None:
            print("incoming_msg.sent_to.id : " + incoming_msg.sent_to.id)
        print("================start of Chat Object ===================")
        print("incoming_msg.chat.id : " + incoming_msg.chat.id)
        print("incoming_msg.chat.title :" + incoming_msg.chat.title)
        print("incoming_msg.chat.name :" + incoming_msg.chat.name)
        print("incoming_msg.chat.type :" + incoming_msg.chat.type)
        print("================End of Chat Object ===================")
        print("================Start of From User Object ===================")
        print("incoming_msg.from.id : " + incoming_msg.from_.id)
        print("incoming_msg.from.name : " + incoming_msg.from_.name)
        print("incoming_msg.from.terminal: " + incoming_msg.from_.terminal)
        print("incoming_msg.from.version : " + incoming_msg.from_.version)
        print("================End of From User Object ===================")

        if incoming_msg.is_text_msg():
            handle_incoming_text_msg(incoming_msg)
