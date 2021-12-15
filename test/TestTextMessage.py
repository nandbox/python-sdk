import json

from NandboxClient import NandboxClient
from data.Button import Button
from nandbox import Nandbox
from util import Utils

CONFIG_FILE = "../config.json"

f = open(CONFIG_FILE)
config = json.load(f)
f.close()

client = NandboxClient.get(config)

nandbox = Nandbox()

napi = nandbox.Api()

CYELLOW = '\033[93m'
CEND = '\033[0m'


def create_button(label, callback, order, bg_color, txt_color, btn_query, next_menu_ref):
    btn = Button({})

    btn.button_label = label
    btn.button_callback = callback
    btn.button_order = order
    btn.button_bgcolor = bg_color
    btn.button_textcolor = txt_color
    btn.button_query = btn_query
    btn.next_menu = next_menu_ref

    return btn


def handle_incoming_text_msg(incoming_msg):
    print("incoming_msg.status " + incoming_msg.status)
    print("incoming_msg.text : " + incoming_msg.text)

    if "3m" == incoming_msg.text:
        chatId = incoming_msg.chat.id

        Utils.set_navigation_button(chat_id=chatId, next_menu="mainMenu", api=napi)


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
        if incoming_msg.sent_to is not None:
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


callBack = nCallBack()
client.connect(config['Token'], callBack)
