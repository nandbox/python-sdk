import json
from idlelib.multicall import r

from docutils.nodes import reference

from nandboxbots.NandboxClient import NandboxClient
from nandboxbots.data.Chat import Chat
from nandboxbots.data.Data import Data
from nandboxbots.data.User import User
from nandboxbots.nandbox import Nandbox
from nandboxbots.outmessages.SetNavigationButtonOutMessage import SetNavigationButtonOutMessage
from nandboxbots.util import Utils

CONFIG_FILE = "../../config.json"

f = open(CONFIG_FILE)
config = json.load(f)
f.close()

client = NandboxClient.get(config)

nandbox = Nandbox()

napi = nandbox.Api()

CYELLOW = '\033[93m'
CEND = '\033[0m'


class nCallBack(nandbox.Callback):
    def on_connect(self, api):
        global napi
        napi = api
        print("Authenticated")
        nv = SetNavigationButtonOutMessage()
        nv.navigation_button = "Menu ID"


    def on_receive(self, incoming_msg):
        print(CYELLOW + "Message Received" + CEND)
        if incoming_msg.is_text_msg():
            chatId = incoming_msg.chat.id
            text = incoming_msg.text
            global napi
            reference = Utils.get_unique_id()
            napi.send_text(chat_id=chatId, text=text, reference=reference,app_id=incoming_msg.app_id)

    def on_white_list_pattern(self, white_list_pattern):
        print(white_list_pattern.to_json_obj())
    def on_my_profile(self, user):
        print(user)
    def on_user_details(self, user):
        print(user.to_json_obj())
    def on_white_list(self, white_list):
        print(white_list.to_json_obj())
    def on_black_list(self, black_list):
        print(black_list.to_json_obj())
    def on_remove_white_list(self,white_list):
        print("here")
        print(white_list.to_json_obj())
    def on_chat_member(self, chat_member):
        print(chat_member.to_json_onj())
    def on_remove_black_list(self, black_list):
        print("here")
        print(black_list.to_json_obj())
    def on_black_list_pattern(self, black_list_pattern):
        print(black_list_pattern.to_json_obj())
    def on_product_detail(self,obj):
        print(obj.to_json_obj())

callBack = nCallBack()
client.connect(config['Token'], callBack)
