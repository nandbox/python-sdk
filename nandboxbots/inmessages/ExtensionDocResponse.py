import json


class ExtensionDocResponse:
    def __init__(self, obj):
        self.id = None
        self.table_name = None
        self.doc = None
        self.ref = None
        self.app_id = None
        self.method = None

        if "doc_id" in obj:
            self.id = obj.get("doc_id")

        if "doc_type" in obj:
            self.table_name = obj.get("doc_type")

        if "doc" in obj:
            try:
                doc_value = obj.get("doc")

                if isinstance(doc_value, dict):
                    self.doc = doc_value
                else:
                    self.doc = json.loads(str(doc_value))

            except Exception:
                self.doc = {}

        if "ref" in obj:
            self.ref = str(obj.get("ref"))

        if "app_id" in obj:
            self.app_id = str(obj.get("app_id"))

        if "method" in obj:
            self.method = str(obj.get("method"))