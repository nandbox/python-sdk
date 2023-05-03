import json

from nandboxbots.NandboxClient import NandboxClient
from nandboxbots.nandbox import Nandbox
from nandboxbots.util import Utils
from nandboxbots.data.WorkflowCell import WorkflowCell

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

    def on_chat_menu_callback(self, chat_menu_callback):
        userId = chat_menu_callback.chat.id
        screenId = chat_menu_callback.menu_ref
        appId = chat_menu_callback.appId
        btnCallback = chat_menu_callback.button_callback

        print(CYELLOW +
              "APP ID:-" + appId + "\n" + "USER ID:-" + userId + "\n" + "SCREEN ID:-" + screenId + "\n" + "BUTTON "
                                                                                                          "CALLBACK:-" + btnCallback + CEND + "\n")
        cell = WorkflowCell({
            "cell_id": "button10",
            "callback": "button10",
            "label": "FROM Ms 5ateer SDK YAY",
            "sublabel": "python sdk yay",
            "bg_color": "#ff0000",
            "label_color": "#ffffff",
            "sublabel_color": "#ffffff"
        }).to_json_obj()

        workflow_cells = [cell]

        global napi
        reference = Utils.get_unique_id()
        napi.set_workflow(userId, screenId, appId, workflow_cells, reference, False)


callBack = nCallBack()
client.connect(config['Token'], callBack)
