from enum import IntEnum


class PriorityEnum(IntEnum):
    """
    Приоритет задачи
    """
    minimum = 0
    low = 1
    medium = 2
    high = 3
    maximum = 4

class StatusEnum(IntEnum):
    """
    Статус выполнения задачи
    """
    pending = 0
    in_progress = 1
    completed = 2
    failed = 3
