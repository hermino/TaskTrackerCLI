import pytest
from task_tracker.task import TaskManager
from task_tracker.storage import Storage

storage = Storage()
task_manager = TaskManager(storage)

@pytest.mark.parametrize("description", [
    ("Walk with dog"),
    ('Clean the house')
])
def test_create_task(description: str):
    task = task_manager.create_task(description)
    assert task["description"] == description

