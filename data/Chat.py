import json

from data.TagDefinition import TagDefinition


class Chat:
    KEY_ID = "id"
    KEY_TITLE = "title"
    KEY_NAME = "name"
    KEY_TYPE = "type"
    KEY_VERSION = "version"
    KEY_LANGUAGE_CODE = "language_code"
    KEY_REGIONS = "regions"
    KEY_DESCRIPTION = "description"
    KEY_PHOTO = "photo"
    KEY_CATEGORY = "category"
    KEY_MEMBER_COUNT = "member_count"
    KEY_INVITE_LINK = "invite_link"
    KEY_TAGS_DEFINITION = "tagsDefinition"

    id = None
    title = None
    name = None
    type = None
    version = None
    language_code = None
    regions = None
    description = None
    photo = None
    category = None
    member_count = None
    invite_link = None
    tags_definition = None

    def __init__(self, dictionary):

        self.id = str(dictionary[self.KEY_ID])
        self.title = str(dictionary[self.KEY_TITLE])
        self.name = str(dictionary[self.KEY_NAME])
        self.type = str(dictionary[self.KEY_TYPE])
        self.version = str(dictionary[self.KEY_VERSION])
        self.language_code = int(dictionary[self.KEY_LANGUAGE_CODE])
        self.regions = str(dictionary[self.KEY_REGIONS])
        self.description = str(dictionary[self.KEY_DESCRIPTION])
        self.category = str(dictionary[self.KEY_CATEGORY])
        self.member_count = int(dictionary[self.KEY_MEMBER_COUNT])
        self.invite_link = str(dictionary[self.KEY_INVITE_LINK])

        tags_arr_obj = dictionary[self.KEY_TAGS_DEFINITION]
        if tags_arr_obj is not None:
            self.tags_definition = [None] * len(tags_arr_obj)
            for i in range(len(tags_arr_obj)):
                self.tags_definition[i] = TagDefinition(tags_arr_obj[i])

    def to_json_obj(self):

        dictionary = {}

        if self.id is not None:
            dictionary[self.KEY_ID] = self.id
        if self.title is not None:
            dictionary[self.KEY_TITLE] = self.title
        if self.name is not None:
            dictionary[self.KEY_NAME] = self.name
        if self.type is not None:
            dictionary[self.KEY_TYPE] = self.type
        if self.version is not None:
            dictionary[self.KEY_VERSION] = self.version
        if self.language_code is not None:
            dictionary[self.KEY_LANGUAGE_CODE] = self.language_code
        if self.regions is not None:
            dictionary[self.KEY_REGIONS] = self.regions
        if self.description is not None:
            dictionary[self.KEY_DESCRIPTION] = self.description
        if self.category is not None:
            dictionary[self.KEY_CATEGORY] = self.category
        if self.member_count is not None:
            dictionary[self.KEY_MEMBER_COUNT] = self.member_count
        if self.invite_link is not None:
            dictionary[self.KEY_INVITE_LINK] = self.invite_link
        if self.photo is not None:
            dictionary[self.KEY_PHOTO] = self.photo

        return json.dumps(dictionary), dictionary
