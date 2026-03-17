from pydantic import BaseModel


class Task(BaseModel):
    """
    Модель задачи.
    Attributes:
        id: Уникальный идентификатор задачи
        payload: Словарь с данными задачи (название, дедлайн, приоритет и т.д.)
    """

    id: str
    payload: dict

    def __repr__(self):
        """
        Строковое представление задачи для отладки.
        Returns:
            str: Представление задачи в формате "Task(id; payload)"
        """
        return f"Task({self.id}; {self.payload})"
