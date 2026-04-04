import pytest
from unittest.mock import MagicMock
from src.tasks_reader import TasksReader
from src.task_sources.task_source_protocol import TaskSource


@pytest.fixture
def mock_source():
    source = MagicMock(spec=TaskSource)
    source.get_tasks.return_value = ["task1", "task2"]
    return source


def test_read_tasks(mock_source):
    reader = TasksReader([mock_source, mock_source])  # type: ignore
    tasks = reader.read_tasks()

    assert tasks == ["task1", "task2", "task1", "task2"]
    assert len(tasks) == 4


def test_reader_manage_sources(mock_source):
    reader = TasksReader([])

    reader.add_source(mock_source)  # type: ignore
    assert reader._sources == [mock_source]

    reader.remove_source_by_index(0)
    assert reader._sources == []


def test_reader_errors():
    reader = TasksReader([])

    for invalid in ["not a source", 123]:
        with pytest.raises(TypeError):
            TasksReader([invalid])  # type: ignore
        with pytest.raises(TypeError):
            reader.add_source(invalid)  # type: ignore

    with pytest.raises(IndexError):
        reader.remove_source_by_index(99)


def test_read_empty():
    assert TasksReader([]).read_tasks() == []
