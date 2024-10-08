import pytest
from task_tracker.task import TaskManager
from task_tracker.storage import Storage

storage = Storage()
task_manager = TaskManager(storage)

@pytest.mark.parametrize("description", [
    ("Walk with dog")
])
def test_store_task(description: str):
    task = task_manager.create_task(description)
    search_task = storage.search(task["id"])

    assert search_task["description"] == description

@pytest.mark.parametrize("id", [
    (1)
])
def test_search_task(id: int):
    task = storage.search(id)
    assert task["id"] == id


@pytest.mark.parametrize("id, description", [
    (1, "Walk with cat")
])
def test_update_task(id: int, description: str):
    task = storage.update_description(id, description)
    assert task["description"] == description


@pytest.mark.parametrize("id", [
    (1)
])
def test_remove_task(id: int):
    storage.remove(id)
    task = storage.search(id)
    assert task == None