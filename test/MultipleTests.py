import json
import os

from NandboxClient import NandboxClient
from data.Button import Button
from data.Data import Data
from data.Menu import Menu
from data.Row import Row
from data.WhiteListUser import WhiteListUser
from nandbox import Nandbox
from outmessages.PhotoOutMessage import PhotoOutMessage
from outmessages.SetChatMenuOutMessage import SetChatMenuOutMessage
from util import Utils
from util import MediaTransfer

CONFIG_FILE = "../config.json"

f = open(CONFIG_FILE)
config = json.load(f)
f.close()

TOKEN = config['Token']

client = NandboxClient.get(config)

nandbox = Nandbox()

napi = nandbox.Api()

CYELLOW = '\033[93m'
CEND = '\033[0m'


def handle_incoming_photo_msg(incoming_msg):
    print(f"================start of Photo Object ===================")
    print(f"incoming_msg.photo.id: {str(incoming_msg.photo.id)}")
    print(f"incoming_msg.photo.width: {str(incoming_msg.photo.width)}")
    print(f"incoming_msg.photo.height: {str(incoming_msg.photo.height)}")
    print(f"incoming_msg.photo.size: {str(incoming_msg.photo.size)}")
    print(f"================start of Photo Thumbnail  Object ===================")

    chatId = incoming_msg.chat.id

    if incoming_msg.photo.thumbnail is not None:
        pass
    else:
        print("================No Thumbnail Object in this Photo ===================")

    napi.generate_permanent_url(incoming_msg.photo.id, "Any Reference")

    MediaTransfer.download_file(TOKEN, incoming_msg.photo.id, f"{os.curdir}/download", None, config['DownloadServer'])

    napi.send_text(chatId,
                   f"Photo size is : {incoming_msg.photo.size} and photo width is : {incoming_msg.photo.width} and photo height is : {incoming_msg.photo.height} and caption is : {incoming_msg.caption} \n\n Wait please sending you a photo ....",
                   Utils.get_unique_id())

    uploaded_photo_id = MediaTransfer.upload_file(TOKEN, f"{os.curdir}/upload/welcome.jpg", config['UploadServer'])

    if uploaded_photo_id is not None:
        photo_msg = PhotoOutMessage()
        photo_msg.chat_id = chatId
        photo_msg.reference = Utils.get_unique_id()
        photo_msg.photo = uploaded_photo_id
        photo_msg.caption = "Photo from Bot"
        photo_msg.echo = 1
        napi.send(photo_msg)


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
        chatId = incoming_msg.chat.id

        if incoming_msg.reply_to_message_id is not None:
            if incoming_msg.is_text_msg():
                incomingText = incoming_msg.text.casefold()

                if incomingText == "getChatMember".casefold():
                    napi.get_chat_member(chatId, incoming_msg.from_.id)

                elif incomingText == "getAdmins".casefold():
                    napi.get_chat_administrators(chatId)

                elif incomingText == "getChat".casefold():
                    napi.get_chat(chatId)

                elif incomingText == "getBlackList".casefold():
                    napi.get_black_list(chatId)

                elif incomingText == "addBlacklistPatterns".casefold():
                    data = Data()
                    data.pattern = "44444*"
                    data.example = "44444444"

                    another_data = Data()
                    another_data.pattern = "222*"
                    another_data.example = "222222222"

                    dataList = [data, another_data]

                    napi.add_black_list_patterns(chatId, dataList)

                elif incomingText == "addWhitelistPatterns".casefold():
                    data = Data()
                    data.pattern = "4444*"
                    data.example = "444444"

                    dataList = [data]

                    napi.add_white_list_patterns(chatId, dataList)

                elif incomingText == "getWhiteList".casefold():
                    napi.get_white_list(chatId)

                elif incomingText == "addBlackList".casefold():
                    users = ["111133", "222223"]
                    napi.add_black_list(chatId, users)

                elif incomingText == "addWhiteList".casefold():
                    tagsList = ["1", "2"]

                    whiteListUser = WhiteListUser()
                    whiteListUser.signup_user = "3636526"
                    whiteListUser.tags = tagsList

                    whiteListUsersArray = [whiteListUser]
                    napi.add_white_list(chatId, whiteListUsersArray)

                elif incomingText == "deleteBlackList".casefold():
                    users = ["111133"]
                    napi.delete_black_list(chatId, users)

                elif incomingText == "deleteWhitelist".casefold():
                    users = ["111133"]
                    napi.delete_white_list(chatId, users)

                elif incomingText == "deleteBlacklistPatterns".casefold():
                    pattern = ["222*"]
                    napi.delete_black_list_patterns(chatId, pattern)

                elif incomingText == "deleteWhitelistPatterns".casefold():
                    pattern = ["5555*"]
                    napi.delete_white_list_patterns(chatId, pattern)

                elif incomingText == "BigText".casefold():
                    napi.send_text_with_background(chatId, "Hi from bot", "#EE82EE")

        else:
            print(f"=========>> {incoming_msg.type} Message Received =========>>")
            print(f"incoming_msg.message_id : {str(incoming_msg.message_id)}")
            print(f"incoming_msg.date : {str(incoming_msg.date)}")
            print(f"incoming_msg.reference : {str(incoming_msg.reference)}")
            print(f"incoming_msg.caption: {str(incoming_msg.caption)}")
            if incoming_msg.sent_to is not None:
                print("incoming_msg.sent_to.id : " + str(incoming_msg.sent_to.id))
            print("================start of Chat Object ===================")
            print(f"incoming_msg.chat.id : {str(chatId)}")
            print(f"incoming_msg.chat.title : {str(incoming_msg.chat.title)}")
            print(f"incoming_msg.chat.name : {str(incoming_msg.chat.name)}")
            print("incoming_msg.chat.type :" + str(incoming_msg.chat.type))
            print("================End of Chat Object ===================")
            print("================Start of From User Object ===================")
            print(f"incoming_msg.from.id : {str(incoming_msg.from_.id)}")
            print(f"incoming_msg.from.name : {str(incoming_msg.from_.name)}")
            print(f"incoming_msg.from.status : {str(incoming_msg.from_.status)}")
            print(f"incoming_msg.from.terminal: {str(incoming_msg.from_.terminal)}")
            print(f"incoming_msg.from.version : {str(incoming_msg.from_.version)}")
            print(f"incoming.msg.from.type : {str(incoming_msg.from_.type)}")
            print("================End of From User Object ===================")

            if incoming_msg.is_text_msg():
                pass
            elif incoming_msg.is_text_file_msg():
                pass
            elif incoming_msg.is_photo_msg():
                pass
            elif incoming_msg.is_video_msg():
                pass
            elif incoming_msg.is_voice_msg():
                pass
            elif incoming_msg.is_article_msg():
                pass
            elif incoming_msg.is_audio_msg():
                pass
            elif incoming_msg.is_gif_msg():
                pass
            elif incoming_msg.is_location_msg():
                pass
            elif incoming_msg.is_contact_msg():
                pass
            elif incoming_msg.is_document_msg():
                pass


callBack = nCallBack()
client.connect(TOKEN, callBack)
