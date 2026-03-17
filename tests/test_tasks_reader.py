from unittest.mock import MagicMock
from src.task import Task
from src.tasks_reader import TasksReader
from src.task_sources.task_source_protocol import TaskSource
from pytest import raises


def test_tasks_reader_combines_tasks():
    source1 = MagicMock(spec=TaskSource)
    source2 = MagicMock(spec=TaskSource)

    task1 = Task(id="1", payload={})
    task2 = Task(id="2", payload={})

    source1.get_tasks.return_value = [task1]
    source2.get_tasks.return_value = [task2]

    reader = TasksReader([source1, source2])
    all_tasks = reader.read_tasks()

    assert len(all_tasks) == 2
    assert all_tasks[0].id == "1"
    assert all_tasks[1].id == "2"


def test_tasks_reader_validation():
    with raises(
        TypeError, match="TasksReader only accepts TaskSource instances"
    ):
        TasksReader(["not a source"])
