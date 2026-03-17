from src.task import Task
from json import load


class TasksFromFile:
    """Получает задачи из JSON-файла."""

    def __init__(self, file_path: str):
        """
        Инициализирует источник задач из файла.
        Args:
            file_path: Путь к JSON-файлу с задачами
        """
        self.json_file_path = file_path

    def get_tasks(self) -> list[Task]:
        """
        Получить список задач из JSON-файла.
        Returns:
            list[Task]: Список задач
        Raises:
            FileNotFoundError: Если файл не найден
            JSONDecodeError: Если файл содержит некорректный JSON
        """
        with open(self.json_file_path, "r", encoding="utf-8") as f:
            data: list[dict] = load(f)
        return [Task(**task) for task in data]
