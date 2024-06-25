from nandboxbots.data.CollectionProduct import CollectionProduct


class GetCollectionProductResponse:
    def __init__(self, obj):
        self.collection_product = CollectionProduct(obj)

    def to_json_obj(self):
        obj = {}
        if self.collection_product is not None:
            obj['collectionProduct'] = self.collection_product.to_json_obj()
        return obj