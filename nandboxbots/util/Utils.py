import uuid

from nandboxbots.outmessages.SetNavigationButtonOutMessage import SetNavigationButtonOutMessage


def get_unique_id():
    return int(uuid.uuid4().hex[:14], base=16)


def to_long(value):
    """Interprets a JSON value as an int, returning 0 when absent or unparseable."""
    if value is None:
        return 0
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        return int(value)
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return 0


def get_fields_and_values(cells):
    """Flattens submitted menu cells into a {callback: value} mapping.

    Mirrors Utils.getFieldsAndValues in the Java SDK: each cell's `callback` is
    the field name and the first entry of its value list is the submitted value.
    """
    result = {}
    if not cells:
        return result
    for cell in cells:
        key = cell.callback
        value_str = ""
        values = cell.value
        if values:
            val = values[0].value
            value_str = "" if val is None else str(val)
        result[key] = value_str
    return result


def to_bool(value):
    """Interprets a JSON value as a boolean.

    Plain bool() is wrong for JSON payloads: bool("false") and bool("0") are both
    True, so a server sending these fields as strings always read as True.
    """
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    return str(value).strip().lower() in ("true", "1", "yes")


def format_date(now):
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
    return dt_string


def set_navigation_button(chat_id, next_menu, api):


    nav_msg = SetNavigationButtonOutMessage()
    nav_msg.chat_id = chat_id
    nav_msg.navigation_button = next_menu
    msg, _ = nav_msg.to_json_obj()

    api.send(msg)


def format_duration(duration):
    if duration is not None:
        millis = int(duration)
        seconds = (millis / 1000) % 60
        seconds = int(seconds)
        minutes = (millis / (1000 * 60)) % 60
        minutes = int(minutes)
        hours = (millis / (1000 * 60 * 60)) % 24
        return "%d:%d:%d" % (hours, minutes, seconds)
    return None


