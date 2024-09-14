import pytest
from task_tracker.task import TaskManager


@pytest.mark.parametrize("description", [
    ("Walk with dog"),
    ('Clean the house')
])
def test_create_task(description: str):
    task = TaskManager.create_task(description)
    assert task.description == description

