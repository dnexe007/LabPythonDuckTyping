from datetime import datetime, timedelta
from typing import Any, Optional, Type, Union
from enum import Enum


class IdValidator:
    """
    Валидатор идентификатора: проверяет, что ID является целым неотрицательным числом.
    """
    def __init__(self) -> None:
        self._name: Optional[str] = None

    def __set_name__(self, owner: Type, name: str) -> None:
        self._name = "_" + name

    def __get__(self, instance: Any, owner: Optional[Type] = None) -> Any:
        if instance is None:
            return self
        return getattr(instance, self._name)  # type: ignore

    def __set__(self, instance: Any, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Id must be an integer")
        if value < 0:
            raise ValueError("Id must be >= 0")
        setattr(instance, self._name, value)  # type: ignore


class EnumValidator:
    """
    Валидатор Enum: проверяет соответствие данных указанному enum,
    в случае несоответствия пробует преобразовать в enum,
    так как это может быть int, подходящий под enum
    """
    def __init__(self, enum_class: type) -> None:
        self._name: Optional[str] = None
        self._enum_class: type = enum_class

    def __set_name__(self, owner: Type, name: str) -> None:
        self._name = "_" + name

    def __get__(self, instance: Any, owner: Optional[Type] = None) -> Any:
        if instance is None:
            return self
        return getattr(instance, self._name)  # type: ignore

    def __set__(self, instance: Any, value: Union[Enum, int]) -> None:
        if not isinstance(value, self._enum_class):
            value = self._enum_class(value)
        setattr(instance, self._name, value)  # type: ignore


class DescriptionValidator:
    """
    Валидатор описания: проверяет тип строки и длину (от 1 до 200 символов).
    """
    def __init__(self) -> None:
        self._name: Optional[str] = None

    def __set_name__(self, owner: Type, name: str) -> None:
        self._name = "_" + name

    def __get__(self, instance: Any, owner: Optional[Type] = None) -> Any:
        if instance is None:
            return self
        return getattr(instance, self._name)  # type: ignore

    def __set__(self, instance: Any, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        if not 1 <= len(value) <= 200:
            raise ValueError("Description must be from 1 to 200 characters")
        setattr(instance, self._name, value)  # type: ignore


class CreatedAtValidator:
    """
    Валидатор даты создания: разрешает установку значения только один раз.
    """
    def __init__(self) -> None:
        self._name: Optional[str] = None

    def __set_name__(self, owner: Type, name: str) -> None:
        self._name = "_" + name

    def __get__(self, instance: Any, owner: Optional[Type] = None) -> Any:
        if instance is None:
            return self
        return getattr(instance, self._name)  # type: ignore

    def __set__(self, instance: Any, value: datetime) -> None:
        if not isinstance(value, datetime):
            raise TypeError("CreatedAt must be a datetime")
        if hasattr(instance, self._name):  # type: ignore
            raise AttributeError("CreatedAt can't be overridden")
        setattr(instance, self._name, value)  # type: ignore


class IsNewDescriptor:
    """
    Дескриптор для проверки, является ли задача новой (создана менее 24 часов назад).
    """
    def __get__(self, instance: Any, owner: Optional[Type] = None) -> Union[bool, "IsNewDescriptor"]:
        if instance is None:
            return self
        delta: timedelta = datetime.now() - instance.created_at
        return delta <= timedelta(hours=24)
