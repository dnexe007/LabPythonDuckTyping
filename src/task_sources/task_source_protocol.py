from typing import Protocol, runtime_checkable
from src.task import Task


@runtime_checkable
class TaskSource(Protocol):
    """Источник задач для получения списка заданий."""

    def get_tasks(self) -> list[Task]:
        """
        Получить список задач.
        Returns:
            list[Task] | None: Список задач или None, если задач нет
        """
        ...
