from unittest.mock import MagicMock
from src.task import Task
from src.tasks_reader import TasksReader
from src.task_sources.task_source_protocol import TaskSource
from pytest import raises


def test_tasks_reader_combines_tasks() -> None:
    source1 = MagicMock(spec=TaskSource)
    source2 = MagicMock(spec=TaskSource)

    task1 = Task(id="1", payload={})
    task2 = Task(id="2", payload={})

    source1.get_tasks.return_value = [task1]
    source2.get_tasks.return_value = [task2]

    reader = TasksReader([source1, source2])  # type: ignore
    all_tasks = reader.read_tasks()

    assert len(all_tasks) == 2
    assert all_tasks[0].id == "1"
    assert all_tasks[1].id == "2"


def test_tasks_reader_validation() -> None:
    with raises(
            TypeError, match="TasksReader only accepts TaskSource instances"
    ):
        TasksReader(["not a source"])  # type: ignore


def test_tasks_reader_add_source() -> None:
    reader = TasksReader([])
    source = MagicMock(spec=TaskSource)

    reader.add_source(source)  # type: ignore

    assert len(reader._sources) == 1
    assert reader._sources[0] is source


def test_tasks_reader_add_source_validation() -> None:
    reader = TasksReader([])
    with raises(TypeError, match="TasksReader only accepts TaskSource instances"):
        reader.add_source("not a source")  # type: ignore


def test_tasks_reader_remove_source() -> None:
    source = MagicMock(spec=TaskSource)
    reader = TasksReader([source])  # type: ignore

    reader.remove_source_by_index(0)

    assert len(reader._sources) == 0


def test_tasks_reader_remove_source_index_error() -> None:
    reader = TasksReader([])
    with raises(IndexError):
        reader.remove_source_by_index(0)
