import json
import os

from nandboxbots.NandboxClient import NandboxClient
from nandboxbots.data.Button import Button
from nandboxbots.data.Menu import Menu
from nandboxbots.data.Row import Row
from nandboxbots.nandbox import Nandbox
from nandboxbots.outmessages.PhotoOutMessage import PhotoOutMessage
from nandboxbots.outmessages.SetChatMenuOutMessage import SetChatMenuOutMessage
from nandboxbots.util import Utils, MediaTransfer

CONFIG_FILE = "../../config.json"


f = open(CONFIG_FILE)
config = json.load(f)
f.close()

TOKEN = config['Token']

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
    print(f"incoming_msg.text : {str(incoming_msg.text)}")

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


def handle_incoming_photo_msg(incoming_msg):
    print(f"================start of Photo Object ===================")
    print(f"incoming_msg.photo.id: {str(incoming_msg.photo.id)}")
    print(f"incoming_msg.photo.width: {str(incoming_msg.photo.width)}")
    print(f"incoming_msg.photo.height: {str(incoming_msg.photo.height)}")
    print(f"incoming_msg.photo.size: {str(incoming_msg.photo.size)}")
    print(f"================start of Photo Thumbnail  Object ===================")

    if incoming_msg.photo.thumbnail is not None:
        pass
    else:
        print("================No Thumbnail Object in this Photo ===================")

    napi.generate_permanent_url(incoming_msg.photo.id, "Any Reference")
    print("Hello")
    MediaTransfer.download_file(TOKEN, incoming_msg.photo.id, f"{os.curdir}/download", None, config['DownloadServer'])
    print("Bello")
    napi.send_text(incoming_msg.chat.id, f"Photo size is : {incoming_msg.photo.size} and photo width is : {incoming_msg.photo.width} and photo height is : {incoming_msg.photo.height} and caption is : {incoming_msg.caption} \n\n Wait please sending you a photo ....", Utils.get_unique_id())

    uploaded_photo_id = MediaTransfer.upload_file(TOKEN, f"{os.curdir}/upload/welcome.jpg", config['UploadServer'])

    if uploaded_photo_id is not None:
        photo_msg = PhotoOutMessage()
        photo_msg.chat_id = incoming_msg.chat.id
        photo_msg.reference = Utils.get_unique_id()
        photo_msg.photo = uploaded_photo_id
        photo_msg.caption = "Photo from Bot"
        photo_msg.echo = 1

        photoJSON, _ = photo_msg.to_json_obj()

        napi.send(photoJSON)


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
            print(f"incoming_msg.sent_to.id : {str(incoming_msg.sent_to.id)}")
        print("================start of Chat Object ===================")
        print(f"incoming_msg.chat.id : {str(incoming_msg.chat.id)}")
        print(f"incoming_msg.chat.title : {str(incoming_msg.chat.title)}")
        print(f"incoming_msg.chat.name : {str(incoming_msg.chat.name)}")
        print(f"incoming_msg.chat.type : {str(incoming_msg.chat.type)}")
        print("================End of Chat Object ===================")
        print("================Start of From User Object ===================")
        print(f"incoming_msg.from.id : {str(incoming_msg.from_.id)}")
        print(f"incoming_msg.from.name : {str(incoming_msg.from_.name)}")
        print(f"incoming_msg.from.terminal: {str(incoming_msg.from_.terminal)}")
        print(f"incoming_msg.from.version : {str(incoming_msg.from_.version)}")
        print("================End of From User Object ===================")

        if incoming_msg.is_text_msg():
            handle_incoming_text_msg(incoming_msg)
        elif incoming_msg.is_photo_msg():
            handle_incoming_photo_msg(incoming_msg)


callBack = nCallBack()
client.connect(TOKEN, callBack)
