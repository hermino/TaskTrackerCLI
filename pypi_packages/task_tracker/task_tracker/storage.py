import json
from .constants import STORAGE


class Storage:

    _ids = None

    @property
    def list(self) -> dict:
        """

        :return:
        """
        with open(STORAGE, "r", encoding="utf-8") as storage:
            tasks = json.load(storage)

            if not self._ids:
                self._ids = set([task["id"] for task in tasks])

        return tasks

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

        if task["id"] not in self._ids:
            current_task.append(task)
            self._ids.add(task["id"])

            with open(STORAGE, "w", encoding="utf-8") as storage:
                json.dump(current_task, storage, ensure_ascii=False, indent=4)

    def update(self, id: int, description: str) -> dict:
        """

        :param id:
        :param description:
        :return:
        """
        task = self.search(id)
        task["description"] = description
        self.store(task)

        return task

    def remove(self, id: int):
        """

        :param id:
        :return:
        """
        update_list = [task for task in self.list if task["id"] != id]

        self._ids.discard(id)

        with open(STORAGE, "w", encoding="utf-8") as storage:
            json.dump(update_list, storage, ensure_ascii=False, indent=4)
