import datetime
import uuid


def get_unique_id():
    return int(uuid.uuid4().hex[:14], base=16)


def format_date(now):
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
    return dt_string


print(get_unique_id())
