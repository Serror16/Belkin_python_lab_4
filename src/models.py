import time
from typing import Any


class TaskInvariantError(ValueError):
    """Генерируется при нарушении инвариантов задачи (неверный статус, приоритет и т.д.)"""
    pass


class ValidatedChoice:
    """Дескриптор данных для валидации значений из заданного списка (например, статуса или приоритета)"""

    def __init__(self, name: str, choices: set[str]):
        self.private_name = f"_{name}"
        self.choices = choices

    def __get__(self, instance, owner) -> Any:
        if instance is None:
            return None
        return getattr(instance, self.private_name)

    def __set__(self, instance, value: str) -> None:
        if value not in self.choices:
            raise TaskInvariantError(f"Недопустимое значение '{value}'. Допустимые варианты: {self.choices}")
        setattr(instance, self.private_name, value)


class ReadOnlyField:
    """Non-data дескриптор, предоставляющий доступ к защищенному полю только для чтения"""

    def __init__(self, name: str):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner) -> Any:
        if instance is None:
            return None
        return getattr(instance, self.private_name)


class Task:
    priority = ValidatedChoice("priority", {"low", "medium", "high", "critical"})
    status = ValidatedChoice("status", {"pending", "in_progress", "completed", "failed"})
    id = ReadOnlyField("id")

    def __init__(self, task_id: int, description: str, priority: str = "medium", status: str = "pending"):
        self._id = task_id
        self.description = description
        self._created_at = time.time()
        self.priority = priority
        self.status = status

    @property
    def description(self) -> str:
        """Свойство для чтения описания"""
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """Описание не может быть пустым"""
        if not value or len(value.strip()) == 0:
            raise TaskInvariantError("Описание задачи не может быть пустым.")
        self._description = value

    @property
    def created_at(self) -> float:
        """Свойство только для чтения"""
        return self._created_at

    @property
    def is_ready(self) -> bool:
        """Готова ли задача к выполнению"""
        return self.status == "pending"

    def __repr__(self) -> str:
        return f"Task: id={self.id} priority={self.priority} status={self.status} ready={self.is_ready}"
