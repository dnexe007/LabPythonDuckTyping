from pytest import raises
from src.task_sources.tasks_generator import TasksGenerator
from src.task import Task


def test_tasks_generator() -> None:
    gen1 = TasksGenerator(5)
    tasks = gen1.get_tasks()
    assert len(tasks) == 5

    for task in tasks:
        assert isinstance(task, Task)
        assert task.payload["title"] in gen1.titles
        assert task.payload["deadline"] in gen1.deadlines
        assert task.payload["priority"] in gen1.priorities

    with raises(TypeError):
        TasksGenerator(-1)

    with raises(TypeError):
        TasksGenerator(5.5)  # type: ignore
