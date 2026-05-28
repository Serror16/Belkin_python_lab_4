from typing import Protocol, runtime_checkable, Iterable
from src.models import Task

@runtime_checkable
class TaskSource(Protocol):
    """Контракт для источников задач"""
    def get_tasks(self) -> Iterable[Task]:
        """Возвращает итерируемый объект с задачами"""
        ...
