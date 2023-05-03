import json

from nandboxbots.data.WorkflowCell import WorkflowCell


class WorkflowDetails:
    __KEY_WORKFLOW_DETAILS = "WorkflowDetails"
    __KEY_WORKFLOW_CELL = "WorkflowCell"

    workflowCell = []

    def __init__(self, dictionary):
        workflow_details_dict = dictionary[
            self.__KEY_WORKFLOW_DETAILS] if self.__KEY_WORKFLOW_DETAILS in dictionary.keys() else {}
        workflow_cell_arr_obj = workflow_details_dict[
            self.__KEY_WORKFLOW_CELL] if self.__KEY_WORKFLOW_CELL in workflow_details_dict.keys() else None
        if workflow_cell_arr_obj is not None:
            length = len(workflow_cell_arr_obj)
            workflowCells = [WorkflowCell({})] * length
            for i in range(length):
                workflowCells[i] = WorkflowCell(workflow_cell_arr_obj[i])

            self.workflowCell = workflowCells

    def to_json_obj(self):
        dictionary = {}
        if self.workflowCell is not None:
            workflow_cell_arr = []
            for i in range(len(self.workflowCell)):
                workflow_cell_arr.append(self.workflowCell[i].to_json_obj())

            dictionary[self.__KEY_WORKFLOW_CELL] = workflow_cell_arr

        return json.dumps(dictionary), dictionary
