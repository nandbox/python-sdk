from nandboxbots.outmessages.SetRecordOutMessage import SetRecordOutMessage
from nandboxbots.outmessages.GetRecordOutMessage import GetRecordOutMessage
from nandboxbots.outmessages.ListRecordsOutMessage import ListRecordsOutMessage
from nandboxbots.outmessages.DeleteRecordOutMessage import DeleteRecordOutMessage


class DatabaseService:
    __instance = None

    @staticmethod
    def get_instance():
        if DatabaseService.__instance is None:
            DatabaseService.__instance = DatabaseService()

        return DatabaseService.__instance

    """
    INSERT OR UPDATE
    """
    def set(self, api, obj, table_name, doc_id, ref):
        out_message = SetRecordOutMessage()

        out_message.table_name = table_name
        out_message.id = doc_id
        out_message.doc = obj
        out_message.ref = ref

        api.send(out_message)

    """
    GET
    """
    def get(self, api, doc_id, table_name, ref):
        out_message = GetRecordOutMessage()

        out_message.table_name = table_name
        out_message.id = doc_id
        out_message.ref = ref

        api.send(out_message)

    """
    DELETE
    """
    def delete(self, api, doc_id, table_name, ref):
        out_message = DeleteRecordOutMessage()

        out_message.table_name = table_name
        out_message.id = doc_id
        out_message.ref = ref

        api.send(out_message)

    """
    LIST
    """
    def list(self, api, table_name, ref):
        out_message = ListRecordsOutMessage()

        out_message.table_name = table_name
        out_message.ref = ref

        api.send(out_message)