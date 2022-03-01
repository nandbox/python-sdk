import json

from nandboxbots.NandboxClient import NandboxClient
from nandboxbots.nandbox import Nandbox
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

    def on_receive(self, incoming_msg):
        print(CYELLOW + "Message Received" + CEND)

        if incoming_msg.is_text_msg():
            chatId = incoming_msg.chat.id
            text = incoming_msg.text
            global napi
            reference = Utils.get_unique_id()
            napi.send_text(chat_id=chatId, text=text, reference=reference)


callBack = nCallBack()
client.connect(config['Token'], callBack)
