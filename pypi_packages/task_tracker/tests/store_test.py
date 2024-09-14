import pytest
from task_tracker.task import TaskManager, Task
from task_tracker.storage import Storage

storage = Storage()


@pytest.mark.parametrize("description", [
    ("Walk with dog")
])
def test_store_task(description: str):
    task = TaskManager.create_task(description)
    b = Task.model_validate(task)
    a = vars(task)
    storage.store(a)
    search = storage.search(task.id)

    assert search.description == description
