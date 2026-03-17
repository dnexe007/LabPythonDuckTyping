from task_sources.tasks_generator import TasksGenerator
from task_sources.tasks_from_file import TasksFromFile
from task_sources.tasks_from_api import TasksFromAPI
from task_sources.task_source_protocol import TaskSource
from src.tasks_reader import TasksReader


def main() -> None:
    """
        создает TaskReader, добавляет в
        него источники и выводит все задачи.
    """
    sources: list[TaskSource] = [
        TasksGenerator(5),
        TasksFromFile("../data.json"),
        TasksFromAPI("http://localhost:8000"),
    ]

    reader = TasksReader(sources)

    for task in reader.read_tasks():
        print(task)


if __name__ == "__main__":
    main()
