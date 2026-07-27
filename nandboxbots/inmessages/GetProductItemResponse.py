import json

from nandboxbots.data.ProductItem import ProductItem


class GetProductItemResponse:
    def __init__(self, obj):
        # The dispatcher passes the raw dict, so attribute access (obj.data)
        # raised AttributeError on every getProductItemResponse.
        data = obj.get("data")
        self.productItem = ProductItem(data) if data else None
        self.app_id = obj.get("app_id")
        self.reference = obj.get("reference")

    def to_json_obj(self):
        obj = {}
        if self.productItem:
            obj['productItem'] = self.productItem.to_json_obj()
        if self.app_id is not None:
            obj['app_id'] = self.app_id
        if self.reference is not None:
            obj['reference'] = self.reference
        return obj
