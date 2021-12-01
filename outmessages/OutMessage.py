import json


class OutMessage:
    WEB_PREVIEW_DISABLE = 1
    WEB_PREVIEW_HIDE_LINK = 2
    WEB_PREVIEW_INSTANCE_VIEW = 3
    WEB_PREVIEW_INSTANCE_WITHOUT_LINK = 4

    KEY_METHOD = "method"
    KEY_CHAT_ID = "chat_id"
    KEY_REFERENCE = "reference"
    KEY_TO_USER_ID = "to_user_id"
    KEY_REPLAY_TO_MESSAGE_ID = "reply_to_message_id"
    KEY_WEB_PAGE_PREVIEW = "web_page_preview"
    KEY_DISABLE_NOTIFICATION = "disable_notification"
    KEY_CAPTION = "caption"
    KEY_ECHO = "echo"
    KEY_MENU_REF = "menu_ref"
    KEY_INLINE_MENU = "inline_menu"
    KEY_CHAT_SETTINGS = "chat_settings"
    KEY_STYLE = "style"
    KEY_SCHEDULE_DATE = "schedule_date"

    method = None
    chat_id = None
    reference = None
    to_user_id = None
    reply_to_message_id = None
    web_page_preview = None
    disable_notification = None
    caption = None
    echo = None
    menu_ref = None
    inline_menus = None
    chat_settings = None
    schedule_date = None

    def to_json_object(self):
        obj = {}

        if self.method is not None:
            obj[self.KEY_METHOD] = self.method
        if self.chat_id is not None:
            obj[self.KEY_CHAT_ID] = self.chat_id
        if self.reference is not None:
            obj[self.KEY_REFERENCE] = self.reference
        if self.to_user_id is not None:
            obj[self.KEY_TO_USER_ID] = self.to_user_id
        if self.reply_to_message_id is not None:
            obj[self.KEY_REPLAY_TO_MESSAGE_ID] = self.reply_to_message_id
        if self.web_page_preview is not None:
            obj[self.KEY_WEB_PAGE_PREVIEW] = self.web_page_preview
        if self.disable_notification is not None:
            obj[self.KEY_DISABLE_NOTIFICATION] = self.disable_notification
        if self.caption is not None:
            obj[self.KEY_CAPTION] = self.caption
        if self.echo is not None:
            obj[self.KEY_ECHO] = self.echo
        if self.menu_ref is not None:
            obj[self.KEY_MENU_REF] = self.menu_ref
        if self.inline_menus is not None:
            inline_menus_array = []
            for i in range(0, len(self.inline_menus)):
                inline_menus_array.append(self.inline_menus.to_json_object)
            obj[self.KEY_INLINE_MENU] = inline_menus_array
        if self.chat_settings is not None:
            obj[self.KEY_CHAT_SETTINGS] = self.chat_settings
        if self.schedule_date is not None:
            obj[self.KEY_SCHEDULE_DATE] = self.schedule_date

        return json.dumps(obj), obj
