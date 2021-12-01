import uuid


def get_unique_id():
    return int(uuid.uuid4().hex[:14], base=16)


print(get_unique_id())
