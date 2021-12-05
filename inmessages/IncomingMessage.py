import json
import logging

from data.Article import Article
from data.Audio import Audio
from data.Chat import Chat
from data.Contact import Contact
from data.Document import Document
from data.Gif import Gif
from data.Location import Location
from data.Photo import Photo
from data.Sticker import Sticker
from data.TextFile import TextFile
from data.User import User
from data.Video import Video
from data.Voice import Voice
from data.WhiteListUser import WhiteListUser


class IncomingMessage:

    KEY_MESSAGE = "message"
    KEY_MESSAGE_ID = "message_id"
    KEY_TYPE = "type"
    KEY_FROM_ADMIN = "from_admin"
    KEY_DATE = "date"
    KEY_TEXT = "text"
    KEY_LOCATION = "location"
    KEY_CONTACT = "contact"
    KEY_DOCUMENT = "document"
    KEY_FROM = "from"
    KEY_CHAT = "chat"
    KEY_REFERENCE = "reference"
    KEY_SENT_TO = "sent_to"
    KEY_PHOTO = "photo"
    KEY_GIF = "gif"
    KEY_VIDEO = "video"
    KEY_AUDIO = "audio"
    KEY_VOICE = "voice"
    KEY_CAPTION = "caption"
    KEY_STICKER = "sticker"
    KEY_REPLY_TO_MESSAGE_ID = "reply_to_message_id"
    KEY_TEXT_FILE = "text_file"
    KEY_STATUS = "status"
    KEY_CHAT_SETTINGS = "chat_settings"
    KEY_BG_COLOR = "bg_color"
    KEY_WHITELIST_USER = "users"
    KEY_ARTICLE = "article"
    KEY_URL = "url"
    KEY_SCHEDULE_DATE = "schedule_date"

    message_id = None
    type = None
    date = None
    reference = None
    from_ = None
    reply_to_message_id = None
    caption = None
    from_admin = None
    chat = None
    text = None
    location = None
    contact = None
    sent_to = None
    photo = None
    gif = None
    voice = None
    video = None
    audio = None
    document = None
    sticker = None
    text_file = None
    status = None
    chat_settings = None
    bg_color = None
    article = None
    url = None
    white_list_user = None
    tag = None
    schedule_date = None

    def __init__(self, dictionary):
        msg_dict = dictionary[self.KEY_MESSAGE]

        from_user = User(msg_dict[self.KEY_FROM])
        sent_to_user = User(msg_dict[self.KEY_SENT_TO]) if msg_dict[self.KEY_SENT_TO] is not None else None

        self.chat = Chat(msg_dict[self.KEY_CHAT]) if msg_dict[self.KEY_CHAT] is not None else None
        self.location = Location(msg_dict[self.KEY_LOCATION]) if msg_dict[self.KEY_LOCATION] is not None else None
        self.contact = Contact(msg_dict[self.KEY_CONTACT]) if msg_dict[self.KEY_CONTACT] is not None else None
        self.document = Document(msg_dict[self.KEY_DOCUMENT]) if msg_dict[self.KEY_DOCUMENT] is not None else None
        self.photo = Photo(msg_dict[self.KEY_PHOTO]) if msg_dict[self.KEY_PHOTO] is not None else None
        self.gif = Gif(msg_dict[self.KEY_GIF]) if msg_dict[self.KEY_GIF] is not None else None
        self.voice = Voice(msg_dict[self.KEY_VOICE]) if msg_dict[self.KEY_VOICE] is not None else None
        self.video = Video(msg_dict[self.KEY_VIDEO]) if msg_dict[self.KEY_VIDEO] is not None else None
        self.audio = Audio(msg_dict[self.KEY_AUDIO]) if msg_dict[self.KEY_AUDIO] is not None else None
        self.article = Article(msg_dict[self.KEY_ARTICLE]) if msg_dict[self.KEY_ARTICLE] is not None else None
        self.sticker = Sticker(msg_dict[self.KEY_STICKER]) if msg_dict[self.KEY_STICKER] is not None else None
        self.text_file = TextFile(msg_dict[self.KEY_TEXT_FILE]) if msg_dict[self.KEY_TEXT_FILE] is not None else None
        self.text = str(msg_dict[self.KEY_TEXT])
        self.message_id = str(msg_dict[self.KEY_MESSAGE_ID])
        self.date = int(str(msg_dict[self.KEY_DATE]))
        self.reference = int(str(msg_dict[self.KEY_REFERENCE]))
        self.from_ = from_user
        self.sent_to = sent_to_user
        self.from_admin = int(msg_dict[self.KEY_FROM_ADMIN])
        self.type = str(msg_dict[self.KEY_TYPE])
        self.caption = str(msg_dict[self.KEY_CAPTION])
        self.url = str(msg_dict[self.KEY_URL])
        self.reply_to_message_id = str(msg_dict[self.KEY_REPLY_TO_MESSAGE_ID])
        self.status = str(self.KEY_STATUS)
        self.chat_settings = int(self.KEY_CHAT_SETTINGS)
        self.bg_color = str(self.KEY_BG_COLOR)
        self.white_list_user = WhiteListUser(msg_dict[self.KEY_WHITELIST_USER]) if msg_dict[self.KEY_WHITELIST_USER] is not None else None
        self.schedule_date = int(str(msg_dict[self.KEY_SCHEDULE_DATE])) if msg_dict[self.KEY_SCHEDULE_DATE] is not None else None

    def to_json_obj(self):

        dictionary = {}

        if self.type is not None:
            dictionary[self.KEY_TYPE] = self.type
        if self.date is not None:
            dictionary[self.KEY_DATE] = self.date
        if self.from_ is not None:
            _, from_dict = self.from_.to_json_obj()
            dictionary[self.KEY_FROM] = from_dict
        if self.chat is not None:
            _, chat_dict = self.chat.to_json_obj()
            dictionary[self.KEY_CHAT] = chat_dict
        if self.message_id is not None:
            dictionary[self.KEY_MESSAGE_ID] = self.message_id
        if self.from_admin is not None:
            dictionary[self.KEY_FROM_ADMIN] = self.from_admin
        if self.status is not None:
            dictionary[self.KEY_STATUS] = self.status
        if self.sent_to is not None:
            _, sent_to_dict = self.sent_to.to_json_obj()
            dictionary[self.KEY_SENT_TO] = sent_to_dict
        if self.reference is not None:
            dictionary[self.KEY_REFERENCE] = self.reference
        if self.caption is not None:
            dictionary[self.KEY_CAPTION] = self.caption
        if self.url is not None:
            dictionary[self.KEY_URL] = self.url
        if self.reply_to_message_id is not None:
            dictionary[self.KEY_REPLY_TO_MESSAGE_ID] = self.reply_to_message_id
        if self.text is not None:
            dictionary[self.KEY_TEXT] = self.text
        if self.location is not None:
            _, location_dict = self.location.to_json_obj()
            dictionary[self.KEY_LOCATION] = location_dict
        if self.contact is not None:
            _, contact_dict = self.contact.to_json_obj()
            dictionary[self.KEY_CONTACT] = contact_dict
        if self.document is not None:
            _, document_dict = self.document.to_json_obj()
            dictionary[self.KEY_DOCUMENT] = document_dict
        if self.photo is not None:
            _, photo_dict = self.photo.to_json_obj()
            dictionary[self.KEY_PHOTO] = photo_dict
        if self.gif is not None:
            _, gif_dict = self.gif.to_json_obj()
            dictionary[self.KEY_GIF] = gif_dict
        if self.voice is not None:
            _, voice_dict = self.voice.to_json_obj()
            dictionary[self.KEY_VOICE] = voice_dict
        if self.video is not None:
            _, video_dict = self.video.to_json_obj()
            dictionary[self.KEY_VIDEO] = video_dict
        if self.audio is not None:
            _, audio_dict = self.audio.to_json_obj()
            dictionary[self.KEY_AUDIO] = audio_dict
        if self.article is not None:
            _, article_dict = self.article.to_json_obj()
            dictionary[self.KEY_ARTICLE] = article_dict
        if self.sticker is not None:
            _, sticker_dict = self.sticker.to_json_obj()
            dictionary[self.KEY_STICKER] = sticker_dict
        if self.text_file is not None:
            _, text_file_dict = self.text_file.to_json_obj()
            dictionary[self.KEY_TEXT_FILE] = text_file_dict
        if self.bg_color is not None:
            dictionary[self.KEY_BG_COLOR] = self.bg_color
        if self.white_list_user is not None:
            _, white_list_user_dict = self.white_list_user.to_json_obj()
            dictionary[self.KEY_WHITELIST_USER] = white_list_user_dict
        if self.schedule_date is not None:
            dictionary[self.KEY_SCHEDULE_DATE] = self.schedule_date

        logging.info("to " + dictionary)

        return json.dumps(dictionary), dictionary










