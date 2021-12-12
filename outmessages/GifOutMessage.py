import enum
import json

from outmessages.OutMessage import OutMessage


class GifOutMessage(OutMessage):
    KEY_PHOTO = "photo"
    KEY_VIDEO = "video"

    class GifType(enum.Enum):
        PHOTO = 1
        VIDEO = 2

    gif = None
    gif_type = GifType.PHOTO

    def __init__(self, gif_type):
        self.gif_type = gif_type

        if gif_type == GifOutMessage.GifType.PHOTO:
            self.method = "sendPhoto"
        elif gif_type == GifOutMessage.GifType.PHOTO:
            self.method = "sendVideo"
        else:
            self.method = "sendPhoto"

    def to_json_obj(self):
        _, dictionary = super(GifOutMessage, self).to_json_obj()

        if self.gif is not None:
            if self.gif_type == GifOutMessage.GifType.PHOTO:
                dictionary[self.KEY_PHOTO] = self.gif
            elif self.gif_type == GifOutMessage.GifType.VIDEO:
                dictionary[self.KEY_VIDEO] = self.gif
            else:
                dictionary[self.KEY_PHOTO] = self.gif

        return json.dumps(dictionary), dictionary

