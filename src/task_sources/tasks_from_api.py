from requests import get

from src.task import Task


class TasksFromAPI:
    """Получает задачи из внешнего API."""

    def __init__(self, url: str):
        """
        Инициализирует источник задач.
        Args:
            url: Адрес API для получения задач
        """
        self.url = url

    def get_tasks(self) -> list[Task]:
        """
        Получает список задач из API.
        Returns:
            list[Task]: Список задач. Может быть пустым.
        Raises:
            HTTPError: Если запрос к API завершился ошибкой.
        """
        response = get(self.url)
        response.raise_for_status()
        data = response.json()
        return [Task(**task) for task in data]
