from random import choice, randint
from datetime import datetime, timedelta

from src.task.model import Task
from src.task.enums import PriorityEnum, StatusEnum


class TasksGenerator:
    """Генерирует случайные задачи, комбинируя данные из списков"""

    def __init__(self, count: int):
        """
        Инициализирует генератор задач.
        Args:
            count: Количество задач для генерации
        Raises:
            TypeError: Если count не является целым неотрицательным числом
        """
        if not isinstance(count, int) or count < 0:
            raise TypeError("count must be a non-negative integer")
        self.count: int = count
        self.descriptions: list[str] = [
            "Fix critical bug in authentication module",
            "Update documentation for API endpoints",
            "Review pull request from team member",
            "Run comprehensive test suite",
            "Deploy application to production",
            "Optimize database queries",
            "Refactor legacy code",
            "Write unit tests for new features",
            "Investigate memory leak issue",
            "Prepare presentation for sprint review"
        ]

    def get_tasks(self) -> list[Task]:
        """
        Сгенерировать список случайных задач.
        Returns:
            list[Task]: Список сгенерированных задач
        """
        tasks: list[Task] = []
        for i in range(self.count):
            hours_delta = randint(0, 100)
            minutes_delta = randint(0, 60)
            created_at = (
                datetime.now() -
                timedelta(
                    hours=hours_delta,
                    minutes=minutes_delta
                )
            )

            task = {
                "id": 1000 + i,
                "description": choice(self.descriptions),
                "priority": randint(PriorityEnum.low, PriorityEnum.maximum),
                "status": randint(StatusEnum.pending, StatusEnum.failed),
                "created_at": created_at.isoformat(),
            }
            tasks.append(Task.from_dict(task))
        return tasks
