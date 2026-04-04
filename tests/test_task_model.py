import pytest
from datetime import datetime, timedelta
from src.task.model import Task
from src.task.enums import PriorityEnum, StatusEnum


def test_task_init():
    dt = datetime(2026, 4, 3)
    task = Task(1, "Test", PriorityEnum.high, StatusEnum.pending, dt)

    assert task.id == 1
    assert task.priority == PriorityEnum.high
    assert task.created_at == dt
    assert "Task(id=1" in repr(task)


def test_task_serialization():
    data = {
        "id": 2, "description": "Dict test",
        "priority": 1, "status": 0,
        "created_at": "2026-04-03T10:00:00"
    }
    task = Task.from_dict(data)
    assert task.to_dict() == data


def test_task_properties():
    now = datetime.now()

    t1 = Task(1, "Ok", PriorityEnum.medium, StatusEnum.pending, now - timedelta(hours=5))
    assert t1.is_new is True
    assert t1.is_ready_to_do is True

    t2 = Task(2, "Low", PriorityEnum.low, StatusEnum.pending, now - timedelta(hours=30))
    assert t2.is_new is False
    assert t2.is_ready_to_do is False


def test_task_validation_errors():
    params = {"id": 1, "description": "Valid", "priority": 1, "status": 0}

    invalid_data = [
        {"id": -1},
        {"description": ""},
        {"priority": 99},
        {"status": 50},
    ]

    for data in invalid_data:
        with pytest.raises(ValueError):
            Task(**{**params, **data})
