import pytest
from json import dumps, JSONDecodeError
from datetime import datetime
from src.task_sources.tasks_from_file import TasksFromFile
from src.task.enums import PriorityEnum, StatusEnum


@pytest.fixture
def create_task_file(tmp_path):
    def _create(name, content):
        file = tmp_path / name
        file.write_text(content if isinstance(content, str) else dumps(content))
        return str(file)

    return _create


def test_file_errors(tmp_path, create_task_file):
    with pytest.raises(FileNotFoundError):
        TasksFromFile(str(tmp_path / "none.json")).get_tasks()

    bad_json = create_task_file("bad.json", "not a json")
    with pytest.raises(JSONDecodeError):
        TasksFromFile(bad_json).get_tasks()


def test_get_tasks_success(create_task_file):
    dt = datetime(2026, 4, 1, 10, 0)
    data = [
        {"id": 1, "description": "T1", "priority": PriorityEnum.medium, "status": StatusEnum.pending,
         "created_at": dt.isoformat()},
        {"id": 2, "description": "T2", "priority": PriorityEnum.low, "status": StatusEnum.completed,
         "created_at": dt.isoformat()}
    ]

    reader = TasksFromFile(create_task_file("tasks.json", data))
    tasks = reader.get_tasks()

    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[0].priority == PriorityEnum.medium
    assert tasks[0].created_at == dt


def test_get_tasks_empty(create_task_file):
    reader = TasksFromFile(create_task_file("empty.json", []))
    assert reader.get_tasks() == []
