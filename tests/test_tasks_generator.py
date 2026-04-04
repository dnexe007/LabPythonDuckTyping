import pytest
from src.task_sources.tasks_generator import TasksGenerator
from src.task.model import Task


def test_tasks_generator_success():
    gen = TasksGenerator(5)
    tasks = gen.get_tasks()

    assert len(tasks) == 5
    assert all(isinstance(t, Task) for t in tasks)
    assert tasks[0].description in gen.descriptions


def test_tasks_generator_invalid_input():
    for val in [-1, 5.5, "5"]:
        with pytest.raises(TypeError):
            TasksGenerator(val)


def test_tasks_generator_zero():
    assert TasksGenerator(0).get_tasks() == []
