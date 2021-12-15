import datetime
import uuid

from data.Button import Button
from outmessages.SetNavigationButtonOutMessage import SetNavigationButtonOutMessage


def get_unique_id():
    return int(uuid.uuid4().hex[:14], base=16)


def format_date(now):
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
    return dt_string


print(get_unique_id())


def set_navigation_button(chat_id, next_menu, api):
    btn = Button({})

    btn.next_menu = next_menu

    nav_msg = SetNavigationButtonOutMessage()
    nav_msg.chat_id = chat_id
    nav_msg.navigation_buttons = []
    nav_msg.navigation_buttons.append(btn)

    msg, _ = nav_msg.to_json_obj()
    api.send(msg)
