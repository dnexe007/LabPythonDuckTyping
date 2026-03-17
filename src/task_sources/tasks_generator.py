from src.task import Task
from random import choice


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
        self.titles: list[str] = ["fix bug", "buy food", "sleep", "talk with deepseek"]
        self.deadlines: list[str] = ["tomorrow", "yesterday", "in week", "in month"]
        self.priorities: list[str] = ["skip", "low", "medium", "high", "maximum"]

    def get_tasks(self) -> list[Task]:
        """
        Сгенерировать список случайных задач.
        Returns:
            list[Task]: Список сгенерированных задач
        """
        tasks: list[Task] = []
        for i in range(self.count):
            payload = {
                "title": choice(self.titles),
                "deadline": choice(self.deadlines),
                "priority": choice(self.priorities),
            }
            task = Task(id=f"generator-{i}", payload=payload)
            tasks.append(task)
        return tasks
