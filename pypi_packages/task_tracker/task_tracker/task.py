from datetime import datetime
from typing import Any


class TaskManager:
    _ids = set()

    def __init__(self, storage: Any):
        self.storage = storage
        self._ids = self.storage.list_ids

    def create_task(self, description: str) -> dict:
        """Create a task

        :param description: description of task
        :return: task created
        """
        try:
            last_id = list(self._ids)[-1] + 1
        except Exception as e:
            print(e)
            last_id = 1

        self._ids.add(last_id)

        task = dict(
            id=last_id,
            description=description,
            status="todo",
            createdAt=datetime.now().isoformat(),
            updatedAt=datetime.now().isoformat()
        )

        self.storage.store(task)
        return task

    def list_task(self, status: int):
        """Action to list of task about status

        :param status: status to list task
        :return: list of task selected
        """
        return [task for task in self.storage.list if task["status"] == status]

    def remove_task(self, tid: int):
        """Remove one task by id

        :param tid: id of task
        """
        self.storage.remove(tid)
        self._ids.discard(id)

    def update_task_description(self, tid: int, description: str):
        """Update description of task

        :param tid: id of task
        :param description: new description of task
        :return: task updated or exception error
        """
        try:
            return self.storage.update_description(tid, description)
        except Exception as e:
            raise Exception(f"This ID doesn't exists: {e}")

    def update_task_status(self, tid: int, status: str):
        """Update status of task

        :param tid: id of task
        :param status: new status of task
        :return: task updated or exception error
        """
        try:
            return self.storage.update_status(tid, status)
        except Exception as e:
            raise Exception(f"This STATUS doesn't exists: {e}")

