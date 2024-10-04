import sys
import pprint
from .storage import Storage
from .task import TaskManager


storage = Storage()
task_manager = TaskManager(storage)

options_status = {
    "mark-done": "done",
    "mark-in-progress": "in-progress"
}

operations = {
    "add": task_manager.create_task,
    "delete": task_manager.remove_task,
    "update": task_manager.update_task_description,
    "mark-done": task_manager.update_task_status,
    "mark-in-progress": task_manager.update_task_status,
    "list": {
        "done": task_manager.list_task("done"),
        "todo": task_manager.list_task("todo"),
        "in-progress": task_manager.list_task("in-progress"),
    }
}


def main():
    """Execution of application

    :return result of operation
    """

    args = args = sys.argv[1:]
    operation = args[0] if len(args) > 0 else None
    arg1 = args[1] if len(args) > 1 else None
    arg2 = args[2] if len(args) > 2 else None

    if (operation and arg1 and arg2) or operation in options_status.keys():
        arg_two = options_status[operation] if operation in options_status.keys() else arg2
        pprint.pprint(operations[operation](int(arg1), arg_two))
    elif operation and arg1:
        if arg1 in ["done", "todo", "in-progress"]:
            pprint.pprint(operations[operation][arg1])
        else:
            pprint.pprint(operations[operation](arg1))
    elif operation == "list":
        pprint.pprint(storage.list)
    else:
        raise Exception("This command doesn't exists!")

