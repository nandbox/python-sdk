import json

from nandboxbots.data.Chat import Chat
from nandboxbots.data.User import User
from nandboxbots.util import Utils


def _as_string(value):
    """Returns None for an absent value instead of the literal string "None"."""
    return None if value is None else str(value)


class CellValue:
    """A single selectable value inside a menu cell."""

    def __init__(self, dictionary=None, value=None, option_label=None):
        if isinstance(dictionary, dict):
            self.id = _as_string(dictionary.get("id"))
            self.value = dictionary.get("value")
            self.option_label = _as_string(dictionary.get("option_label"))
        else:
            # (id, value, option_label) form, used for scalar cell values.
            self.id = _as_string(dictionary)
            self.value = value
            self.option_label = _as_string(option_label)

    def to_json_obj(self):
        dictionary = {}
        if self.id is not None:
            dictionary["id"] = self.id
        if self.value is not None:
            dictionary["value"] = self.value
        if self.option_label is not None:
            dictionary["option_label"] = self.option_label
        return json.dumps(dictionary), dictionary


class ValueType:
    """Wraps a cell's value_type, sent either as a bare string or as {"data": ...}."""

    def __init__(self, data=None):
        self.data = _as_string(data)

    def to_json_obj(self):
        dictionary = {"data": self.data}
        return json.dumps(dictionary), dictionary


class Cell:
    """One cell of a submitted menu form."""

    def __init__(self, dictionary=None):
        dictionary = dictionary or {}
        self.menu_id = _as_string(dictionary.get("menu_id"))
        self.cell_id = _as_string(dictionary.get("cell_id"))
        self.form = _as_string(dictionary.get("form"))
        self.style = _as_string(dictionary.get("style"))
        self.label = _as_string(dictionary.get("label"))
        self.callback = _as_string(dictionary.get("callback"))

        value_type_obj = dictionary.get("value_type")
        if isinstance(value_type_obj, dict):
            data = value_type_obj.get("data")
            self.value_type = ValueType(data) if data is not None else None
        elif value_type_obj is not None:
            self.value_type = ValueType(value_type_obj)
        else:
            self.value_type = None

        value_obj = dictionary.get("value")
        if isinstance(value_obj, list):
            self.value = [CellValue(item) for item in value_obj if isinstance(item, dict)]
        elif isinstance(value_obj, dict):
            self.value = [CellValue(value_obj)]
        elif value_obj is not None:
            self.value = [CellValue(None, value_obj, None)]
        else:
            self.value = None

    def to_json_obj(self):
        dictionary = {}
        if self.menu_id is not None:
            dictionary["menu_id"] = self.menu_id
        if self.cell_id is not None:
            dictionary["cell_id"] = self.cell_id
        if self.form is not None:
            dictionary["form"] = self.form
        if self.style is not None:
            dictionary["style"] = self.style
        if self.label is not None:
            dictionary["label"] = self.label
        if self.callback is not None:
            dictionary["callback"] = self.callback
        if self.value_type is not None:
            _, value_type_dict = self.value_type.to_json_obj()
            dictionary["value_type"] = value_type_dict
        if self.value is not None:
            dictionary["value"] = [v.to_json_obj()[1] for v in self.value]
        return json.dumps(dictionary), dictionary


class MenuCallback:
    """Inbound `menuCallback` event: the values a user submitted from a menu."""

    __KEY_MENU_ID = "menu_id"
    __KEY_MENU_GROUP = "menu_group"
    __KEY_SOURCE = "source"
    __KEY_API_ID = "api_id"
    __KEY_APP_ID = "app_id"
    __KEY_CHAT = "chat"
    __KEY_FROM = "from"
    __KEY_DATE = "date"
    __KEY_CELLS = "cells"

    def __init__(self, dictionary=None):
        dictionary = dictionary or {}
        self.menu_id = _as_string(dictionary.get(self.__KEY_MENU_ID))
        self.menu_group = _as_string(dictionary.get(self.__KEY_MENU_GROUP))
        self.source = _as_string(dictionary.get(self.__KEY_SOURCE))
        self.api_id = _as_string(dictionary.get(self.__KEY_API_ID))
        self.app_id = _as_string(dictionary.get(self.__KEY_APP_ID))
        self.chat = Chat(dictionary[self.__KEY_CHAT]) if dictionary.get(self.__KEY_CHAT) else None
        self.from_ = User(dictionary[self.__KEY_FROM]) if dictionary.get(self.__KEY_FROM) else None
        self.date = Utils.to_long(dictionary.get(self.__KEY_DATE))

        cells = dictionary.get(self.__KEY_CELLS)
        self.cells = [Cell(item) for item in cells if isinstance(item, dict)] if isinstance(cells, list) else None

    def to_json_obj(self):
        dictionary = {}
        if self.menu_id is not None:
            dictionary[self.__KEY_MENU_ID] = self.menu_id
        if self.menu_group is not None:
            dictionary[self.__KEY_MENU_GROUP] = self.menu_group
        if self.source is not None:
            dictionary[self.__KEY_SOURCE] = self.source
        if self.api_id is not None:
            dictionary[self.__KEY_API_ID] = self.api_id
        if self.app_id is not None:
            dictionary[self.__KEY_APP_ID] = self.app_id
        if self.chat is not None:
            _, chat_dict = self.chat.to_json_obj()
            dictionary[self.__KEY_CHAT] = chat_dict
        if self.from_ is not None:
            _, from_dict = self.from_.to_json_obj()
            dictionary[self.__KEY_FROM] = from_dict
        dictionary[self.__KEY_DATE] = self.date
        if self.cells is not None:
            dictionary[self.__KEY_CELLS] = [c.to_json_obj()[1] for c in self.cells]
        return json.dumps(dictionary), dictionary
