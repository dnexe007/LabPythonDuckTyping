import pytest
from requests.exceptions import HTTPError
from datetime import datetime
from src.task_sources.tasks_from_api import TasksFromAPI
from src.task.enums import PriorityEnum, StatusEnum

URL = "https://fake-api.com"

def test_tasks_from_api_success(requests_mock):
    dt = datetime(2026, 4, 3, 10, 30)
    mock_data = [{
        "id": 1, "description": "Fix bug", "priority": PriorityEnum.maximum,
        "status": StatusEnum.pending, "created_at": dt.isoformat()
    }]
    requests_mock.get(URL, json=mock_data)

    tasks = TasksFromAPI(URL).get_tasks()

    assert len(tasks) == 1
    assert tasks[0].id == 1
    assert tasks[0].created_at == dt


def test_tasks_from_api_errors(requests_mock):
    source = TasksFromAPI(URL)

    requests_mock.get(URL, status_code=404)
    with pytest.raises(HTTPError):
        source.get_tasks()

    requests_mock.get(URL, json=[])
    assert source.get_tasks() == []
