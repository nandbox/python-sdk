import json


class Button:
    KEY_BUTTON_SPAN = "button_span"
    KEY_BUTTON_ORDER = "button_order"
    KEY_BUTTON_TEXT_COLOR = "button_textcolor"
    KEY_BUTTON_BG_COLOR = "button_bgcolor"
    KEY_BUTTON_CALLBACK = "button_callback"
    KEY_BUTTON_LABEL = "button_label"
    KEY_BUTTON_URL = "button_url"
    KEY_BUTTON_QUERY = "button_query"
    KEY_NEXT_MENU = "next_menu"
    KEY_CHAT = "chat"
    KEY_BUTTON_ICON = "button_icon"
    KEY_BUTTON_ICON_BG_COLOR = "button_icon_bgcolor"
    BUTTON_QUERY_LOCATION = "location"
    BUTTON_QUERY_CONTACT = "contact"
    KEY_BUTTON_NAV_TYPE = "nav_type"

    button_span = None
    button_order = None
    button_textcolor = None
    button_bgcolor = None
    button_callback = None
    button_label = None
    button_url = None
    button_query = None
    next_menu = None
    chat = None
    button_icon = None
    button_icon_bgcolor = None
    location = None
    contact = None
    nav_type = None

    def __init__(self, dictionary):
        self.button_order = int(dictionary[self.KEY_BUTTON_ORDER])
        self.button_span = int(dictionary[self.KEY_BUTTON_SPAN])
        self.button_textcolor = str(dictionary[self.KEY_BUTTON_TEXT_COLOR])
        self.button_bgcolor = str(dictionary[self.KEY_BUTTON_BG_COLOR])
        self.button_callback = str(dictionary[self.KEY_BUTTON_CALLBACK])
        self.button_label = str(dictionary[self.KEY_BUTTON_LABEL])
        self.button_url = str(dictionary[self.KEY_BUTTON_URL])
        self.button_query = str(dictionary[self.KEY_BUTTON_QUERY])
        self.next_menu = str(dictionary[self.KEY_NEXT_MENU])
        self.chat = str(dictionary[self.KEY_CHAT])
        self.button_icon = str(dictionary[self.KEY_BUTTON_ICON])
        self.button_icon_bgcolor = str(dictionary[self.KEY_BUTTON_ICON_BG_COLOR])
        self.nav_type = str(dictionary[self.KEY_BUTTON_NAV_TYPE])

    def to_json_obj(self):

        dictionary = {}

        if self.button_order is not None:
            dictionary[self.KEY_BUTTON_ORDER] = self.button_order
        if self.button_span is not None:
            dictionary[self.KEY_BUTTON_SPAN] = self.button_span
        if self.button_label is not None:
            dictionary[self.KEY_BUTTON_LABEL] = self.button_label
        if self.button_callback is not None:
            dictionary[self.KEY_BUTTON_CALLBACK] = self.button_callback
        if self.button_url is not None:
            dictionary[self.KEY_BUTTON_URL] = self.button_url
        if self.button_bgcolor is not None:
            dictionary[self.KEY_BUTTON_BG_COLOR] = self.button_bgcolor
        if self.button_textcolor is not None:
            dictionary[self.KEY_BUTTON_TEXT_COLOR] = self.button_textcolor
        if self.button_icon is not None:
            dictionary[self.KEY_BUTTON_ICON] = self.button_icon
        if self.button_icon_bgcolor is not None:
            dictionary[self.KEY_BUTTON_ICON_BG_COLOR] = self.button_icon_bgcolor
        if self.button_query is not None:
            dictionary[self.KEY_BUTTON_QUERY] = self.button_query
        if self.next_menu is not None:
            dictionary[self.KEY_NEXT_MENU] = self.next_menu
        if self.chat is not None:
            dictionary[self.KEY_CHAT] = self.chat
        if self.nav_type is not None:
            dictionary[self.KEY_BUTTON_NAV_TYPE] = self.nav_type

        return json.dumps(dictionary), dictionary
