from multiprocessing import Process
from time import sleep
from uvicorn import run
from os import path
from src.task_sources.tasks_generator import TasksGenerator
from src.task_sources.tasks_from_file import TasksFromFile
from src.task_sources.tasks_from_api import TasksFromAPI
from src.task_sources.task_source_protocol import TaskSource
from src.tasks_reader import TasksReader
from src.api import app


def run_api() -> None:
    """Функция для запуска API в отдельном процессе"""
    run(app, host="localhost", port=8000, log_level="warning")


def main() -> None:
    """
    создает TaskReader, добавляет в
    него источники и выводит все задачи.
    """
    api_process = Process(target=run_api)
    api_process.start()

    sleep(1)

    try:
        sources: list[TaskSource] = [
            TasksGenerator(5),
            TasksFromFile(path.join(path.dirname(__file__), "../data.json")),
            TasksFromAPI("http://localhost:8000"),
        ]

        reader = TasksReader(sources)

        for task in reader.read_tasks():
            print(task)

    finally:
        api_process.terminate()
        api_process.join()


if __name__ == "__main__":
    main()
