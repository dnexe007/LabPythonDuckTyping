from pytest import raises
from src.task_sources.tasks_from_api import TasksFromAPI
from src.task import Task
from requests.exceptions import HTTPError


def test_tasks_from_api_success(requests_mock) -> None:
    url = "https://fake-api.com"
    mock_data = [
        {
            "id": "api-1",
            "payload": {"title": "API Task", "deadline": "now", "priority": "high"},
        }
    ]
    requests_mock.get(url, json=mock_data, status_code=200)

    source = TasksFromAPI(url)
    tasks = source.get_tasks()

    assert len(tasks) == 1
    assert tasks[0].id == "api-1"
    assert isinstance(tasks[0], Task)


def test_tasks_from_api_server_error(requests_mock) -> None:
    url = "https://fake-api.com"
    requests_mock.get(url, status_code=404)

    source = TasksFromAPI(url)

    with raises(HTTPError):
        source.get_tasks()
