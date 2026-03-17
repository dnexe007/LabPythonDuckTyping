from src.task import Task
from src.task_sources.task_source_protocol import TaskSource


class TasksReader:
    def __init__(self, sources: list[TaskSource]):
        """
        Инициализирует читатель задач.
        Args:
            sources: Список источников задач
        Raises:
            TypeError: Если любой из элементов не является TaskSource
        """
        for i in sources:
            if not isinstance(i, TaskSource):
                raise TypeError("TasksReader only accepts TaskSource instances.")
        self.sources = sources

    def read_tasks(self) -> list[Task]:
        """
        Прочитать задачи из всех источников.
        Returns:
            list[Task]: Объединенный список задач из всех источников
        """
        tasks: list[Task] = []
        for source in self.sources:
            tasks.extend(source.get_tasks())
        return tasks
