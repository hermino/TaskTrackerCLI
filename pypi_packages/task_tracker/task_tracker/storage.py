import json
from .constants import STORAGE
from .task import Task

class Storage:
    @property
    def list(self) -> dict:
        """

        :return:
        """
        with open(STORAGE, "r", encoding="utf-8") as storage:
            data = json.load(storage)

        return data

    def search(self, id: int):
        """

        :param id:
        :return:
        """
        return next((Task(**data) for data in self.list if data["id"] == id), None)

    def store(self, data: dict):
        """

        :param data:
        :return:
        """
        current_data = self.list
        current_data.append(data)

        with open(STORAGE, "w", encoding="utf-8") as storage:
            json.dump(current_data, storage, ensure_ascii=False, indent=4)
