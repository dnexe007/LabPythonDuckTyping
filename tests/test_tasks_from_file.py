from pytest import raises
from src.task_sources.tasks_from_file import TasksFromFile
from json import JSONDecodeError, dumps
from src.task import Task


def test_file_not_found_raises_error(tmp_path) -> None:
    file_path = tmp_path / "not_found.json"
    reader = TasksFromFile(str(file_path))
    with raises(FileNotFoundError):
        reader.get_tasks()


def test_invalid_json_raises_error(tmp_path) -> None:
    bad_json = tmp_path / "bad.json"
    bad_json.write_text("not a json", encoding="utf-8")

    reader = TasksFromFile(str(bad_json))
    with raises(JSONDecodeError):
        reader.get_tasks()


def test_tasks_from_file_success(tmp_path) -> None:
    data = [
        {
            "id": "file-001",
            "payload": {
                "title": "Clean up",
                "deadline": "tomorrow",
                "priority": "medium",
            },
        },
        {
            "id": "file-002",
            "payload": {"title": "Walk", "deadline": "today", "priority": "skip"},
        },
    ]

    task_file = tmp_path / "tasks.json"
    task_file.write_text(dumps(data), encoding="utf-8")

    reader = TasksFromFile(str(task_file))
    tasks = reader.get_tasks()

    assert len(tasks) == 2
    assert isinstance(tasks[0], Task)
    assert tasks[0].id == "file-001"
    assert tasks[1].payload["title"] == "Walk"
