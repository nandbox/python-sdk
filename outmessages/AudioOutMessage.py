import json

from outmessages.OutMessage import OutMessage


class AudioOutMessage(OutMessage):
    KEY_AUDIO = "audio"
    KEY_PERFORMER = "performer"
    KEY_TITLE = "title"

    audio = None
    performer = None
    title = None

    def __init__(self):
        self.method = "sendAudio"

    def to_json_obj(self):
        _, dictionary = super(AudioOutMessage, self).to_json_obj()

        if self.audio is not None:
            dictionary[self.KEY_AUDIO] = self.audio
        if self.performer is not None:
            dictionary[self.KEY_PERFORMER] = self.performer
        if self.title is not None:
            dictionary[self.KEY_TITLE] = self.title

        return json.dumps(dictionary), dictionary
