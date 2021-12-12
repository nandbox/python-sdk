import json

from outmessages.OutMessage import OutMessage


class TextOutMessage(OutMessage):
    KEY_TEXT = "text"
    KEY_BG_COLOR = "bg_color"

    text = None
    bg_color = None

    def __init__(self):
        self.method = "sendMessage"

    def to_json_obj(self):
        _, obj = super(TextOutMessage, self).to_json_object()

        if self.text is not None:
            obj[self.KEY_TEXT] = self.text
        if self.bg_color is not None:
            obj[self.KEY_BG_COLOR] = self.bg_color

        return json.dumps(obj), obj
