from src.task.model import Task
from src.task_sources.task_source_protocol import TaskSource


class TasksReader:
    def __init__(self, sources: list[TaskSource] | None = None):
        """
        Инициализирует читатель задач.
        Args:
            sources: Список источников задач
        Raises:
            TypeError: Если любой из элементов не является TaskSource
        """
        if sources is None:
            self._sources = []
            return
        for i in sources:
            if not isinstance(i, TaskSource):
                raise TypeError("TasksReader only accepts TaskSource instances.")
        self._sources = sources.copy()

    def add_source(self, source: TaskSource) -> None:
        """
        Добавить новый источник задач в список.
        Args:
            source: Источник задач для добавления
        Raises:
            TypeError: Если переданный объект не является TaskSource
        """
        if not isinstance(source, TaskSource):
            raise TypeError("TasksReader only accepts TaskSource instances.")
        self._sources.append(source)

    def remove_source_by_index(self, index: int) -> None:
        """
        Удалить источник из списка по его индексу.
        Args:
            index: Индекс удаляемого источника
        Raises:
            IndexError: Если индекс выходит за пределы списка
        """
        self._sources.pop(index)

    def read_tasks(self) -> list[Task]:
        """
        Прочитать задачи из всех источников.
        Returns:
            list[Task]: Объединенный список задач из всех источников
        """
        tasks: list[Task] = []
        for source in self._sources:
            tasks.extend(source.get_tasks())
        return tasks
