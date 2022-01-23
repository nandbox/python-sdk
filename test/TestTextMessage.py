import json

from NandboxClient import NandboxClient
from data.Button import Button
from data.Menu import Menu
from data.Row import Row
from nandbox import Nandbox
from outmessages.SetChatMenuOutMessage import SetChatMenuOutMessage
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
    print(f"incoming_msg.status {str(incoming_msg.status)}")
    print("incoming_msg.text : {str(incoming_msg.text)}")

    if "3m" == incoming_msg.text:
        chatId = incoming_msg.chat.id

        Utils.set_navigation_button(chat_id=chatId, next_menu="mainMenu", api=napi)

        menuBtn1 = create_button('Main', 'mainCB', 1, 'Gray', 'Red', None, None)
        menuBtn2 = create_button('Funny', 'funnyCB', 1, 'Gray', 'Red', None, None)
        menuBtn3 = create_button('Option', 'optionCB', 1, 'Gray', 'Red', None, None)

        outMessage = SetChatMenuOutMessage()

        firstRow = Row()
        firstRow.row_order = 1
        _, btn_dict1 = menuBtn1.to_json_obj()
        _, btn_dict2 = menuBtn3.to_json_obj()
        _, btn_dict3 = menuBtn2.to_json_obj()
        firstRow.buttons.append(btn_dict1)
        firstRow.buttons.append(btn_dict2)
        firstRow.buttons.append(btn_dict3)
        _, row_dict = firstRow.to_json_obj()

        chatMenu = {
            'menu_ref': 'mainMenu',
            'rows': [row_dict]
        }

        outMessage.chat_id = incoming_msg.chat.id
        menu = Menu(chatMenu)
        _, menu_dict = menu.to_json_obj()
        outMessage.menus.append(menu_dict)
        msg, _ = outMessage.to_json_obj()
        napi.send(msg)


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
        print(f"=========>> {incoming_msg.type} Message Received =========>>")
        print(f"incoming_msg.message_id : {str(incoming_msg.message_id)}")
        print(f"incoming_msg.date : {str(incoming_msg.date)}")
        print(f"incoming_msg.reference : {str(incoming_msg.reference)}")
        print(f"incoming_msg.caption: {str(incoming_msg.caption)}")
        if incoming_msg.sent_to is not None:
            print("incoming_msg.sent_to.id : " + str(incoming_msg.sent_to.id))
        print("================start of Chat Object ===================")
        print(f"incoming_msg.chat.id : {str(incoming_msg.chat.id)}")
        print(f"incoming_msg.chat.title : {str(incoming_msg.chat.title)}")
        print(f"incoming_msg.chat.name : {str(incoming_msg.chat.name)}")
        print("incoming_msg.chat.type :" + str(incoming_msg.chat.type))
        print("================End of Chat Object ===================")
        print("================Start of From User Object ===================")
        print(f"incoming_msg.from.id : {str(incoming_msg.from_.id)}")
        print(f"incoming_msg.from.name : {str(incoming_msg.from_.name)}")
        print(f"incoming_msg.from.terminal: {str(incoming_msg.from_.terminal)}")
        print(f"incoming_msg.from.version : {str(incoming_msg.from_.version)}")
        print("================End of From User Object ===================")

        if incoming_msg.is_text_msg():
            handle_incoming_text_msg(incoming_msg)


callBack = nCallBack()
client.connect(config['Token'], callBack)
