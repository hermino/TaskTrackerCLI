import json
from datetime import datetime
from typing import Any
from .constants import STORAGE


class Storage:
    @property
    def list(self) -> dict:
        """List all task

        :return: list of task
        """
        with open(STORAGE, "r", encoding="utf-8") as storage:
            tasks = json.load(storage)
        return tasks

    @property
    def list_ids(self):
        """List all ids

        :return: a set of ids of task
        """
        return set(task["id"] for task in self.list)

    @staticmethod
    def save(list_data: list):
        """Save on task

        :param list_data:
        """
        with open(STORAGE, "w", encoding="utf-8") as storage:
            json.dump(list_data, storage, ensure_ascii=False, indent=4)

    def search(self, tid: int):
        """Search task by id

        :param tid: id of task
        :return: task founded
        """
        return next((task for task in self.list if task["id"] == tid), None)

    def store(self, task: dict):
        """Store data about task

        :param task: task to storage
        """
        current_task = self.list
        current_task.append(task)

        self.save(current_task)

    def remove(self, tid: int):
        """Remove one task of database

        :param tid: id of task
        """
        update_list = [task for task in self.list if task["id"] != int(tid)]
        self.save(update_list)

    def update(self, tid: int, key: str, value: Any):
        """Update task

        :param tid: id of task
        :param key: key of field to change
        :param value: value to change in task
        :return: task changed
        """
        task = self.search(tid)
        task[key] = value
        task["updatedAt"] = datetime.now().isoformat()

        self.remove(tid)
        self.store(task)

        return task

    def update_description(self, tid: int, description: str) -> dict:
        """Update data description about one task

        :param tid: id of one task
        :param description: new description to change
        :return: task changed
        """

        return self.update(tid, "description", description)

    def update_status(self, tid: int, status: str) -> dict:
        """Update data status about one task

        :param tid: id of task
        :param status: status to change on task
        :return: task changed
        """

        return self.update(tid, "status", status)
