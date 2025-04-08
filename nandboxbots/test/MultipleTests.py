#90091783781508815:90090684288020977:O5xSu8TMl2kM2SutEl1T6YezXAEGDO
import json
import os

from nandboxbots.NandboxClient import NandboxClient
from nandboxbots.data.Button import Button
from nandboxbots.data.Data import Data
from nandboxbots.data.Menu import Menu
from nandboxbots.data.Row import Row
from nandboxbots.data.WhiteListUser import WhiteListUser
from nandboxbots.nandbox import Nandbox
from nandboxbots.outmessages.ArticleOutMessage import ArticleOutMessage
from nandboxbots.outmessages.AudioOutMessage import AudioOutMessage
from nandboxbots.outmessages.ContactOutMessage import ContactOutMessage
from nandboxbots.outmessages.DocumentOutMessage import DocumentOutMessage
from nandboxbots.outmessages.GifOutMessage import GifOutMessage
from nandboxbots.outmessages.LocationOutMessage import LocationOutMessage
from nandboxbots.outmessages.OutMessage import OutMessage
from nandboxbots.outmessages.PhotoOutMessage import PhotoOutMessage
from nandboxbots.outmessages.SetChatMenuOutMessage import SetChatMenuOutMessage
from nandboxbots.outmessages.TextOutMessage import TextOutMessage
from nandboxbots.outmessages.VideoOutMessage import VideoOutMessage
from nandboxbots.outmessages.VoiceOutMessage import VoiceOutMessage
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


def create_button(label, callback, order, bg_color, txt_color, btn_query=None, next_menu_ref=None):
    btn = Button({})

    btn.button_label = label
    btn.button_callback = callback
    btn.button_order = order
    btn.button_bgcolor = bg_color
    btn.button_textcolor = txt_color
    btn.button_query = btn_query
    btn.next_menu = next_menu_ref

    return btn


def handle_incoming_photo_msg(incoming_msg):
    print(f"{CYELLOW}================Start of Photo Object ==================={CEND}")
    print(f"incoming_msg.photo.id: {str(incoming_msg.photo.id)}")
    print(f"incoming_msg.photo.width: {str(incoming_msg.photo.width)}")
    print(f"incoming_msg.photo.height: {str(incoming_msg.photo.height)}")
    print(f"incoming_msg.photo.size: {str(incoming_msg.photo.size)}")

    chatId = incoming_msg.chat.id

    if incoming_msg.photo.thumbnail is not None:
        print(f"{CYELLOW}================Start of Photo Thumbnail  Object ==================={CEND}")
        print(f"incoming_msg.photo.thumbnail.id : {str(incoming_msg.photo.thumbnail.id)}")
        print(f"incoming_msg.photo.thumbnail.width : {str(incoming_msg.photo.thumbnail.width)}")
        print(f"incoming_msg.photo.thumbnail.height : {str(incoming_msg.photo.thumbnail.height)}")
        print(f"{CYELLOW}================End of Photo Thumbnail  Object ==================={CEND}")
    else:
        print("================No Thumbnail Object in this Photo ===================")
    print(f"{CYELLOW}================End of Photo Object ==================={CEND}")

    napi.generate_permanent_url(incoming_msg.photo.id, "Any Reference")

    MediaTransfer.download_file(TOKEN, incoming_msg.photo.id, f"{os.curdir}/download", None, config['DownloadServer'])

    napi.send_text(chatId,
                   f"Photo size is : {str(incoming_msg.photo.size)}, photo width is : {str(incoming_msg.photo.width)}, photo height is : {str(incoming_msg.photo.height)}, and caption is : {str(incoming_msg.caption)} \n\n Wait please sending you a photo ....",
                   Utils.get_unique_id())

    uploaded_photo_id = MediaTransfer.upload_file(TOKEN, f"{os.curdir}/upload/welcome.jpg", config['UploadServer'])

    if uploaded_photo_id is not None:
        photo_msg = PhotoOutMessage()
        photo_msg.chat_id = chatId
        photo_msg.reference = Utils.get_unique_id()
        photo_msg.photo = uploaded_photo_id
        photo_msg.caption = "Photo from Bot"
        photo_msg.echo = 1

        photoJSON, _ = photo_msg.to_json_obj()

        napi.send(photoJSON)


def handle_incoming_text_file_msg(incoming_msg):
    textFileId = incoming_msg.text_file.id
    print(f"{CYELLOW}================Start of TextFile Object==================={CEND}")
    print(f"incoming_msg.text : {str(incoming_msg.text)}")
    print(f"incoming_msg.text_file.id : {str(textFileId)}")
    print(f"incoming_msg.text_file.size : {str(incoming_msg.text_file.size)}")
    print(f"{CYELLOW}================End of TextFile Object==================={CEND}")

    MediaTransfer.download_file(TOKEN, textFileId, f"{os.curdir}/download", None, config['DownloadServer'])

    uploadedTextFileId = MediaTransfer.upload_file(TOKEN, f"{os.curdir}/download/{textFileId}", config['UploadServer'])

    napi.send_document(chat_id=incoming_msg.chat.id,
                       document_file_id=uploadedTextFileId,
                       reference=Utils.get_unique_id(),
                       caption="Text File Caption")


def handle_incoming_video_msg(incoming_msg):
    print(f"{CYELLOW}================Start of Video Object==================={CEND}")
    print(f"incoming_msg.video.id : {str(incoming_msg.video.id)}")
    print(f"incoming_msg.video.width : {str(incoming_msg.video.width)}")
    print(f"incoming_msg.video.height : {str(incoming_msg.video.height)}")
    print(f"incoming_msg.video.size : {str(incoming_msg.video.size)}")
    print(f"incoming_msg.video.duration : {str(incoming_msg.video.duration)}")
    if incoming_msg.video.thumbnail is not None:
        print(f"{CYELLOW}================Start of Video Thumbnail  Object ==================={CEND}")
        print(f"incoming_msg.video.thumbnail.id  : {str(incoming_msg.video.thumbnail.id)}")
        print(f"incoming_msg.video.thumbnail.width  : {str(incoming_msg.video.thumbnail.width)}")
        print(f"incoming_msg.video.thumbnail.height : {str(incoming_msg.video.thumbnail.height)}")
        print(f"{CYELLOW}================End of Video Thumbnail Object ==================={CEND}")
    else:
        print("================No Thumbnail Object in this Video ===================")
    print(f"{CYELLOW}================End of Video Object ==================={CEND}")

    uploadedVideoId = MediaTransfer.upload_file(TOKEN, f"{os.curdir}/upload/recallTest.mp4", config['UploadServer'])

    if uploadedVideoId is not None:
        vidMsg = VideoOutMessage()
        vidMsg.chat_id = incoming_msg.chat.id
        vidMsg.reference = Utils.get_unique_id()
        vidMsg.video = uploadedVideoId
        vidMsg.caption = "Video From Bot"
        vidMsg.echo = 0

        vidJSON, _ = vidMsg.to_json_obj()

        napi.send(vidJSON)

    napi.send_text(chat_id=incoming_msg.chat.id,
                   text=f"Video size is : {str(incoming_msg.video.size)}, video width is : {str(incoming_msg.video.width)}, video height is : {str(incoming_msg.video.height)}, video duration is : {str(Utils.format_duration(incoming_msg.video.duration))}, and caption is : {str(incoming_msg.caption)}",
                   reference=Utils.get_unique_id())


def handle_incoming_voice_msg(incoming_msg):
    print(f"{CYELLOW}================Start of Voice Object==================={CEND}")
    print(f"incoming_msg.voice.id : {str(incoming_msg.voice.id)}")
    print(f"incoming_msg.voice.duration : {str(incoming_msg.voice.duration)}")
    print(f"incoming_msg.voice.size : {str(incoming_msg.voice.size)}")
    print(f"{CYELLOW}================End of Voice Object==================={CEND}")

    voiceMsg = VoiceOutMessage()
    voiceMsg.chat_id = incoming_msg.chat.id
    voiceMsg.reference = Utils.get_unique_id()
    voiceMsg.voice = incoming_msg.voice.id
    voiceMsg.size = incoming_msg.voice.size
    voiceMsg.caption = "Voice from Bot"

    voiceJSON, _ = voiceMsg.to_json_obj()

    napi.send(voiceJSON)

    napi.send_text(chat_id=incoming_msg.chat.id,
                   text=f"Voice size is : {str(incoming_msg.voice.size)} and voice Duration is : {str(Utils.format_duration(incoming_msg.voice.duration))}",
                   reference=Utils.get_unique_id())


def handle_incoming_article_msg(incoming_msg):
    print(f"{CYELLOW}================Start of Article Object==================={CEND}")
    print(f"incoming_msg.article.url : {str(incoming_msg.article.url)}")
    print(f"{CYELLOW}================End of Article Object==================={CEND}")

    articleMsg = ArticleOutMessage()
    articleMsg.chat_id = incoming_msg.chat.id
    articleMsg.reference = Utils.get_unique_id()
    articleMsg.url = incoming_msg.url

    articleJSON, _ = articleMsg.to_json_obj()

    napi.send(articleJSON)


def handle_incoming_audio_msg(incoming_msg):
    print(f"{CYELLOW}================Start of Audio Object ==================={CEND}")
    print(f"incoming_msg.audio.id : {str(incoming_msg.audio.id)}")
    print(f"incoming_msg.audio.duration : {str(incoming_msg.audio.duration)}")
    print(f"incoming_msg.audio.title : {str(incoming_msg.audio.title)}")
    print(f"incoming_msg.audio.size : {str(incoming_msg.audio.size)}")
    print(f"incoming_msg.audio.performer : {str(incoming_msg.audio.performer)}")
    print(f"{CYELLOW}================End of Audio Object ==================={CEND}")

    audioMsg = AudioOutMessage()
    audioMsg.chat_id = incoming_msg.chat.id
    audioMsg.reference = Utils.get_unique_id()
    audioMsg.audio = incoming_msg.audio.id
    audioMsg.performer = "Performer Man"
    audioMsg.title = "Song"
    audioMsg.caption = "Audio from Bot"

    audioJSON, _ = audioMsg.to_json_obj()

    napi.send(audioJSON)
    napi.send_text(chat_id=incoming_msg.chat.id,
                   text=f"Audio title : {str(incoming_msg.audio.title)}, audio performer is : {str(incoming_msg.audio.performer)}, audio size is : {str(incoming_msg.audio.size)}, and audio duration is : {str(Utils.format_duration(incoming_msg.audio.duration))}",
                   reference=Utils.get_unique_id())


def handle_incoming_gif_msg(incoming_msg):
    print(f"{CYELLOW}================Start of Gif Object==================={CEND}")
    print(f"incoming_msg.gif.id : {str(incoming_msg.gif.id)}")
    print(f"incoming_msg.gif.width : {str(incoming_msg.gif.width)}")
    print(f"incoming_msg.gif.height : {str(incoming_msg.gif.height)}")
    print(f"incoming_msg.gif.size : {str(incoming_msg.gif.size)}")

    if incoming_msg.gif.thumbnail is not None and incoming_msg.gif.id.endswith(".gif"):
        print(f"{CYELLOW}================Start of Gif Thumbnail  Object ==================={CEND}")
        print(f"incoming_msg.gif.thumbnail.id : {str(incoming_msg.gif.thumbnail.id)}")
        print(f"incoming_msg.gif.thumbnail.width : {str(incoming_msg.gif.thumbnail.width)}")
        print(f"incoming_msg.gif.thumbnail.height : {str(incoming_msg.gif.thumbnail.height)}")
        print(f"{CYELLOW}================End of Gif Thumbnail  Object ==================={CEND}")
        print(f"{CYELLOW}================End of Gif Object==================={CEND}")

        napi.send_text(chat_id=incoming_msg.chat.id,
                       text=f"Gif size is : {str(incoming_msg.gif.size)}, gif width is : {str(incoming_msg.gif.width)}, gif height is : {str(incoming_msg.gif.height)}, and caption is : {str(incoming_msg.caption)}\n\n Wait please sending you a Gif....",
                       reference=Utils.get_unique_id())

        uploadedGifPhotoId = MediaTransfer.upload_file(TOKEN, f"{os.curdir}/upload/gif_sample.gif",
                                                       config['UploadServer'])

        if uploadedGifPhotoId is not None:
            gifMsg = GifOutMessage(GifOutMessage.GifType.PHOTO)
            gifMsg.chat_id = incoming_msg.chat.id
            gifMsg.reference = Utils.get_unique_id()
            gifMsg.gif = uploadedGifPhotoId
            gifMsg.caption = "Gif from Bot"
            gifMsg.echo = 0

            gifJSON, _ = gifMsg.to_json_obj()

            napi.send(gifJSON)

            napi.send_gif(chat_id=incoming_msg.chat.id,
                          caption="with ref",
                          gif_file_id=f"{uploadedGifPhotoId}.gif",
                          reference=Utils.get_unique_id())
        elif incoming_msg.gif.thumbnail is not None and incoming_msg.gif.id.endswith("mp4"):
            print(f"{CYELLOW}================Start of Gif Thumbnail  Object ==================={CEND}")
            print(f"incoming_msg.gif.thumbnail.id : {str(incoming_msg.gif.thumbnail.id)}")
            print(f"incoming_msg.gif.thumbnail.width : {str(incoming_msg.gif.thumbnail.width)}")
            print(f"incoming_msg.gif.thumbnail.height : {str(incoming_msg.gif.thumbnail.height)}")
            print(f"{CYELLOW}================End of Gif Thumbnail  Object ==================={CEND}")
            print(f"{CYELLOW}================End of Gif Object==================={CEND}")

            uploadedGifVideoId = MediaTransfer.upload_file(TOKEN, f"{os.curdir}/upload/CreateGroup.mov",
                                                           config['UploadServer'])

            if uploadedGifVideoId is not None:
                gifMsg = GifOutMessage(GifOutMessage.GifType.VIDEO)
                gifMsg.chat_id = incoming_msg.chat.id
                gifMsg.reference = Utils.get_unique_id()
                gifMsg.gif = uploadedGifVideoId
                gifMsg.caption = "Gif from Bot"
                gifMsg.echo = 0

                gifJSON, _ = gifMsg.to_json_obj()

                napi.send(gifJSON)

                napi.send_gif_video(chat_id=incoming_msg.chat.id,
                                    gif_file_id=uploadedGifVideoId,
                                    caption="with ref",
                                    reference=Utils.get_unique_id())

        else:
            print("================No Thumbnail Object in this Gif===================")


def handle_incoming_location_msg(incoming_msg):
    print(f"{CYELLOW}================Start of Location Object==================={CEND}")
    print(f"incoming_msg.location.name : {str(incoming_msg.location.name)}")
    print(f"incoming_msg.location.details : {str(incoming_msg.location.details)}")
    print(f"incoming_msg.location.latitude : {str(incoming_msg.location.latitude)}")
    print(f"incoming_msg.location.longitude : {str(incoming_msg.location.longitude)}")
    print(f"{CYELLOW}================End of Location Object==================={CEND}")

    locationMsg = LocationOutMessage()
    locationMsg.chat_id = incoming_msg.chat.id
    locationMsg.reference = Utils.get_unique_id()
    locationMsg.name = incoming_msg.location.name
    locationMsg.details = incoming_msg.location.details
    locationMsg.latitude = incoming_msg.location.latitude
    locationMsg.longitude = incoming_msg.location.longitude
    locationMsg.caption = "Location from Bot"

    locationJSON, _ = locationMsg.to_json_obj()

    napi.send(locationJSON)

    napi.send_location(chat_id=incoming_msg.chat.id,
                       latitude=incoming_msg.location.latitude,
                       longitude=incoming_msg.location.longitude,
                       reference=Utils.get_unique_id())

    napi.send_text(chat_id=incoming_msg.chat.id,
                   text=f"Latitude is : {str(incoming_msg.location.latitude)}, longitude is : {str(incoming_msg.location.longitude)}, name is : {str(incoming_msg.location.name)}, and details is : {str(incoming_msg.location.details)}",
                   reference=Utils.get_unique_id())


def handle_incoming_contact_msg(incoming_msg):
    print(f"{CYELLOW}================Start of Contact Object==================={CEND}")
    print(f"incoming_msg.contact.name : {str(incoming_msg.contact.name)}")
    print(f"incoming_msg.contact.phone_number : {str(incoming_msg.contact.phone_number)}")
    print(f"{CYELLOW}================End of Contact Object==================={CEND}")

    contactMsg = ContactOutMessage()
    contactMsg.chat_id = incoming_msg.chat.id
    contactMsg.reference = Utils.get_unique_id()
    contactMsg.name = incoming_msg.contact.name
    contactMsg.phone_number = incoming_msg.contact.phone_number

    contactJSON, _ = contactMsg.to_json_obj()

    napi.send(contactJSON)

    napi.send_contact(chat_id=incoming_msg.chat.id,
                      phone_number=incoming_msg.contact.phone_number,
                      name=incoming_msg.contact.name,
                      reference=Utils.get_unique_id())

    napi.send_text(chat_id=incoming_msg.chat.id,
                   text=f"Contact name is : {str(incoming_msg.contact.name)} Phone number is : {str(incoming_msg.contact.phone_number)}",
                   reference=Utils.get_unique_id())


def handle_incoming_document_msg(incoming_msg):
    print(f"{CYELLOW}================Start of Document Object==================={CEND}")
    print(f"incoming_msg.document.id : {str(incoming_msg.document.id)}")
    print(f"incoming_msg.document.name : {str(incoming_msg.document.name)}")
    print(f"incoming_msg.document.size : {str(incoming_msg.document.size)}")
    print(f"{CYELLOW}================End of Document Object==================={CEND}")

    documentMsg = DocumentOutMessage()
    documentMsg.chat_id = incoming_msg.chat.id
    documentMsg.reference = Utils.get_unique_id()
    documentMsg.document = incoming_msg.document.id
    documentMsg.name = "Document renamed inside Bot"
    documentMsg.caption = "Document From Bot"

    documentJSON, _ = documentMsg.to_json_obj()

    napi.send(documentJSON)

    uploadedDocumentId = MediaTransfer.upload_file(TOKEN, f"{os.curdir}/upload/welcome.jpg", config['UploadServer'])

    napi.send_document(chat_id=incoming_msg.chat.id,
                       document_file_id=uploadedDocumentId,
                       caption="Document caption",
                       reference=Utils.get_unique_id())

    napi.send_text(chat_id=incoming_msg.chat.id,
                   text=f"Document size : {str(incoming_msg.document.size)}, document file name is : {str(incoming_msg.document.name)}, document file id : {str(incoming_msg.document.id)}",
                   reference=Utils.get_unique_id())


class nCallBack(nandbox.Callback):
    def on_product_detail(self,productItem):
        print(productItem.to_json_obj())
    def on_collection_product(self,collectionProducts):
        print(collectionProducts)
    def on_collection_item(self,collectionItem):
        print(collectionItem)
    def on_connect(self, api):
        global napi
        napi = api
        # napi.get_chat_member(chat_id=90089893511487086, user_id=90089893511487086)
        # napi.get_product_detail("5121691410126519")
        # napi.get_chat("90090684261974255")
        # napi.get_user("90089584752198136")
        print("Connected")

    def on_close(self):
        print("Closed")

    def on_error(self):
        print("Error")

    def on_receive(self, incoming_msg):
        chatId = incoming_msg.chat.id
        napi.get_chat_member(chatId, incoming_msg.from_.id)

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
                print(f"incoming_msg.sent_to.id : {str(incoming_msg.sent_to.id)}")
            print(f"{CYELLOW}================start of Chat Object==================={CEND}")
            print(f"incoming_msg.chat.id : {str(chatId)}")
            print(f"incoming_msg.chat.title : {str(incoming_msg.chat.title)}")
            print(f"incoming_msg.chat.name : {str(incoming_msg.chat.name)}")
            print(f"incoming_msg.chat.type : {str(incoming_msg.chat.type)}")
            print(f"{CYELLOW}================End of Chat Object==================={CEND}")
            print(f"{CYELLOW}================Start of From User Object==================={CEND}")
            print(f"incoming_msg.from.id : {str(incoming_msg.from_.id)}")
            print(f"incoming_msg.from.name : {str(incoming_msg.from_.name)}")
            print(f"incoming_msg.from.status : {str(incoming_msg.from_.status)}")
            print(f"incoming_msg.from.terminal: {str(incoming_msg.from_.terminal)}")
            print(f"incoming_msg.from.version : {str(incoming_msg.from_.version)}")
            print(f"incoming.msg.from.type : {str(incoming_msg.from_.type)}")
            print(f"{CYELLOW}================End of From User Object ==================={CEND}")

            if incoming_msg.is_text_msg():
                incomingText = incoming_msg.text
                if incomingText.startswith("Tab"):
                    tabId = incomingText.split()[1]
                    text = f"Tab ID is {str(tabId)}"
                    print(text)
                    reference = Utils.get_unique_id()
                    napi.send_text(chat_id=chatId, text=text, reference=reference, tab=tabId)
                    return

                elif incomingText == "getMyProfile".casefold():
                    napi.get_my_profiles()

                elif incomingText == "getChat".casefold():
                    napi.get_chat(chatId)

                elif incomingText == "getUser".casefold():
                    napi.get_user(incoming_msg.from_.id)

                elif incomingText.casefold() == "1bc".casefold():
                    outMsg = TextOutMessage()
                    reference = Utils.get_unique_id()
                    outMsg.chat_id = chatId
                    outMsg.reference = reference
                    outMsg.text = "https://edition.cnn.com/"
                    outMsg.web_page_preview = OutMessage.WEB_PREVIEW_INSTANCE_VIEW
                    outMsg.echo = 1

                    oneBtn = create_button(label="Visit a Milestone", callback="oneBtnCBInWebView", order=1,
                                           bg_color="RED", txt_color="White")
                    oneBtn.button_icon = "ic_ball_ic_24dp"
                    oneBtn.button_icon_bgcolor = "#FFFF44"

                    firstRow = Row()
                    firstRow.row_order = 1
                    firstRow.buttons = [oneBtn]

                    menuRef = "MAIN_MENU_001"

                    inlineMenu = Menu()
                    inlineMenu.menu_ref = menuRef
                    inlineMenu.rows = [firstRow]

                    outMsg.menu_ref = menuRef
                    outMsg.inline_menus = [inlineMenu]
                    outMsg.app_id=incoming_msg.app_id
                    napi.send(outMsg)

                elif incomingText.casefold() == "3bc".casefold():
                    outMsg = TextOutMessage()
                    reference = Utils.get_unique_id()
                    outMsg.chat_id = chatId
                    outMsg.reference = reference
                    outMsg.text = "https://edition.cnn.com/"
                    outMsg.web_page_preview = OutMessage.WEB_PREVIEW_INSTANCE_VIEW
                    outMsg.echo = 1

                    oneBtn = create_button(label="Visit a Milestone", callback="oneBtnCBInWebView", order=1,
                                           bg_color="RED", txt_color="White")
                    secondBtn = create_button(label="Cairo Porto Mall", callback="secondBtn", order=1, bg_color="RED",
                                              txt_color="White")
                    thirdBtn = create_button(label="Seven Stars Mall", callback="thirdBtn", order=1, bg_color="RED",
                                             txt_color="White")

                    oneBtn.button_url = "https://edition.cnn.com/"

                    firstRow = Row()
                    firstRow.row_order = 1
                    firstRow.buttons = [oneBtn, secondBtn, thirdBtn]

                    menuRef = "MAIN_MENU_001"

                    inlineMenu = Menu()
                    inlineMenu.menu_ref = menuRef
                    inlineMenu.rows = [firstRow]

                    outMsg.menu_ref = menuRef
                    outMsg.inline_menus = [inlineMenu]

                    napi.send(outMsg)

                elif incomingText.casefold() == "buttonIcon".casefold():
                    outMsg = TextOutMessage()
                    outMsg.reference = Utils.get_unique_id()
                    outMsg.text = "https://edition.cnn.com/"
                    outMsg.web_page_preview = OutMessage.WEB_PREVIEW_INSTANCE_VIEW
                    outMsg.echo = 1

                    oneBtn = create_button(label="RSS", callback="oneBtnCBInWebView", order=1, bg_color="RED",
                                           txt_color="White")
                    oneBtn.button_icon = "ic_mood_bad_24dp"
                    oneBtn.button_icon_bgcolor = "#FFFF44"

                    secondBtn = create_button(label="Calendar", callback="secondBtn", order=1, bg_color="RED",
                                              txt_color="White")
                    secondBtn.button_icon = "ic_hourglass_full_24dp"
                    secondBtn.button_icon_bgcolor = "White"

                    thirdBtn = create_button(label="Feed", callback="thirdBtn", order=1, bg_color="RED",
                                             txt_color="White")
                    thirdBtn.button_icon = "ic_credit_card_24dp"
                    thirdBtn.button_icon_bgcolor = "Yellow"
                    thirdBtn.button_url = "https://edition.cnn.com/"

                    firstRow = Row()
                    firstRow.row_order = 1
                    firstRow.buttons = [oneBtn, secondBtn, thirdBtn]

                    menuRef = "MAIN_MENU_001"

                    inlineMenu = Menu()
                    inlineMenu.menu_ref = menuRef
                    inlineMenu.rows = [firstRow]

                    outMsg.menu_ref = menuRef
                    outMsg.inline_menus = [inlineMenu]

                    napi.send(outMsg)

                elif incomingText.casefold() == "3m".casefold():
                    Utils.set_navigation_button(chatId, "mainMenu", napi)

                    menuBtn1 = create_button(label="مصراوي", callback="mainCB", order=1, bg_color="Gray",
                                             txt_color="Red")
                    menuBtn1.button_icon = "ic_smoke_free_24dp"
                    menuBtn1.button_icon_bgcolor = "#00FFFF"

                    menuBtn2 = create_button(label="Funny", callback="funnyCB", order=1, bg_color="Gray",
                                             txt_color="Red")
                    menuBtn2.button_icon = "ic_timeline_24dp"

                    menuBtn3 = create_button(label="Option", callback="optionCB", order=1, bg_color="Gray",
                                             txt_color="Red")
                    menuBtn3.button_icon = "ic_pregnant_woman_24dp"
                    menuBtn3.button_icon_bgcolor = "orange"

                    outMsg = SetChatMenuOutMessage()

                    firstRow = Row()
                    firstRow.row_order = 1
                    firstRow.buttons = [menuBtn1, menuBtn2, menuBtn3]

                    menuRef = "mainMenu"

                    chatMenu = Menu()
                    chatMenu.menu_ref = menuRef
                    chatMenu.rows = [firstRow]

                    outMsg.chat_id = chatId
                    outMsg.menus = [chatMenu]
                    outMsg.app_id=incoming_msg.app_id
                    napi.send(outMsg)

                else:
                    napi.send_text(chat_id=chatId, text=incomingText, reference=Utils.get_unique_id())
            if incoming_msg.from_.id == TOKEN.split(":")[0]:
                return
            elif incoming_msg.is_text_file_msg():
                handle_incoming_text_file_msg(incoming_msg)

            elif incoming_msg.is_photo_msg():
                handle_incoming_photo_msg(incoming_msg)

            elif incoming_msg.is_video_msg():
                handle_incoming_video_msg(incoming_msg)

            elif incoming_msg.is_voice_msg():
                handle_incoming_voice_msg(incoming_msg)

            elif incoming_msg.is_article_msg():
                handle_incoming_article_msg(incoming_msg)

            elif incoming_msg.is_audio_msg():
                handle_incoming_audio_msg(incoming_msg)

            elif incoming_msg.is_gif_msg():
                handle_incoming_gif_msg(incoming_msg)

            elif incoming_msg.is_location_msg():
                handle_incoming_location_msg(incoming_msg)

            elif incoming_msg.is_contact_msg():
                handle_incoming_contact_msg(incoming_msg)

            elif incoming_msg.is_document_msg():
                handle_incoming_document_msg(incoming_msg)


callBack = nCallBack()
client.connect(TOKEN, callBack)
