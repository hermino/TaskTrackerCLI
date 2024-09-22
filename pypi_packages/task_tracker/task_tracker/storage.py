import json
from .constants import STORAGE


class Storage:
    @property
    def list(self) -> dict:
        """

        :return:
        """
        with open(STORAGE, "r", encoding="utf-8") as storage:
            tasks = json.load(storage)
        return tasks

    @property
    def list_ids(self):
        """

        :return:
        """
        return set(task["id"] for task in self.list)

    @staticmethod
    def save(list_data: list):
        """

        :param list_data:
        :return:
        """
        with open(STORAGE, "w", encoding="utf-8") as storage:
            json.dump(list_data, storage, ensure_ascii=False, indent=4)

    def search(self, id: int):
        """

        :param id:
        :return:
        """
        return next((task for task in self.list if task["id"] == id), None)

    def store(self, task: dict):
        """

        :param task:
        :return:
        """
        current_task = self.list
        current_task.append(task)

        self.save(current_task)

    def remove(self, id: int):
        """

        :param id:
        :return:
        """
        update_list = [task for task in self.list if task["id"] != id]
        self.save(update_list)

    def update(self, id: int, description: str) -> dict:
        """

        :param id:
        :param description:
        :return:
        """
        task = self.search(id)
        task["description"] = description

        self.remove(id)
        self.store(task)

        return task

    def update_status(self, id: int, status: int) -> dict:
        """

        :param id:
        :param status:
        :return:
        """
        task = self.search(id)
        task["status"] = status
        self.remove(id)
        self.store(task)

        return task
