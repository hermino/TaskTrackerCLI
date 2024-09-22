from datetime import datetime
from typing import Any

class TaskManager:
    _ids = set()

    def __init__(self, storage: Any):
        self.storage = storage
        self._ids = self.storage.list_ids

    def create_task(self, description: str) -> dict:
        """Create a task

        :param description:
        :return:
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
            status=1,
            createdAt=datetime.now().isoformat(),
            updatedAt=datetime.now().isoformat()
        )

        self.storage.store(task)
        return task

    def list_task(self, status: int):
        """

        :param status:
        :return:
        """
        return [task for task in self.storage.list if task["status"] == status]

    def remove_task(self, tid: int):
        """

        :param tid:
        :return:
        """
        self.storage.remove(tid)
        self._ids.discard(id)

    def update_task_description(self, tid: int, description: str):
        """

        :param tid:
        :param description:
        :return:
        """
        return self.storage.update(tid, description)

    def update_task_status(self, tid: int, status: int):
        """

        :param tid:
        :param status:
        :return:
        """
        return self.storage.update_status(tid, status)
