from datetime import datetime
from typing import Any, Dict, Optional
from .enums import PriorityEnum, StatusEnum
from .validators import IdValidator, DescriptionValidator, EnumValidator, CreatedAtValidator, IsNewDescriptor


class Task:
    """
    Представляет модель задачи с валидацией полей через дескрипторы.

    Хранит id, описание, приоритет, статус выполнения
    и время создания задачи.
    """
    id = IdValidator()
    description = DescriptionValidator()
    priority = EnumValidator(PriorityEnum)
    status = EnumValidator(StatusEnum)
    created_at = CreatedAtValidator()

    is_new = IsNewDescriptor()

    @property
    def is_ready_to_do(self) -> bool:
        """
        Проверяет, готова ли задача к исполнению
        (статус 'в ожидании' и приоритет не ниже среднего).
        """
        return (
            self.status == StatusEnum.pending
            and
            self.priority >= PriorityEnum.medium
        )

    def __init__(
        self,
        id: int,
        description: str,
        priority: PriorityEnum | int,
        status: StatusEnum | int,
        created_at: Optional[datetime] = None
    ) -> None:
        """Инициализирует новый экземпляр задачи."""
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status
        self.created_at = datetime.now() if created_at is None else created_at

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта задачи."""
        return (
            f"Task(id={self.id},"
            f"description={self.description!r},"
            f"priority={self.priority},"
            f"status={self.status},"
            f"created_at={self.created_at})"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Преобразует объект задачи в словарь."""
        return {
            "id": self.id,
            "description": self.description,
            "priority": int(self.priority),
            "status": int(self.status),
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """Создает экземпляр задачи из словаря."""
        return cls(
            id=data["id"],
            description=data["description"],
            priority=data["priority"],
            status=data["status"],
            created_at=datetime.fromisoformat(data["created_at"])
        )
