from tools.read_tasks import read_tasks
from tools.insert_task import insert_task
from tools.delete_task import delete_task
from tools.update_task import update_task

def execute_tool(name, args):
    if name == "read_tasks":
        return read_tasks()

    if name == "insert_task":
        return insert_task(args["title"])

    if name == "delete_task":
        return delete_task(args["task_id"])

    if name == "update_task":
        return update_task(args["task_id"], args["title"])