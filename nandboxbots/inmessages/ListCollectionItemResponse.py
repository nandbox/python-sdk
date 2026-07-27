import json
from nandboxbots.data.Category import Category

class ListCollectionItemResponse:
    def __init__(self, category_list):
        # The dispatcher passes the raw dict, so attribute access
        # (category_list.collections) raised AttributeError on every response.
        collections = category_list.get("collections") or []
        self.categories = [Category(category_dict) for category_dict in collections]
        self.reference = category_list.get("reference")
        self.business_channel_id = category_list.get("business_channel_id")

    def to_json_obj(self):
        # Returns a dictionary suitable for converting to JSON
        return {
            'collections': [category.to_json_obj() for category in self.categories]
        }
