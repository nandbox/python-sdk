from nandboxbots.data.CollectionProduct import CollectionProduct

class GetCollectionProductResponse:
    def __init__(self, obj_list):
        # Subscripts raised KeyError on any partial response.
        self.collection_products = [CollectionProduct(item) for item in (obj_list.get("products") or [])]
        self.app_id = obj_list.get("app_id")
        self.reference = obj_list.get("reference")
    def to_json_obj(self):
        return [product.to_json_obj() for product in self.collection_products]
