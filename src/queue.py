from typing import Iterable, List, Iterator
from src.models import Task
from src.logger_setup import logger

class TaskQueue:
    """Пользовательская коллекция для хранения и фильтрации задач"""

    def __init__(self):
        self._tasks: List[Task] = []
        logger.debug("Создана пустая очередь TaskQueue")

    def add_task(self, task: Task) -> None:
        """Добавляет задачу в очередь с проверкой типа"""

        if not isinstance(task, Task):
            logger.error(f"Попытка добавить некорректный объект в очередь: {type(task)}")
            raise TypeError("Объект должен быть экземпляром класса Task")
        self._tasks.append(task)
        logger.debug(f"Задача {task.id} добавлена в очередь")

    def __iter__(self) -> Iterator[Task]:
        """Реализация итерации"""

        logger.debug("Начало итерации по TaskQueue")
        for task in self._tasks:
            yield task

    def filter_by_priority(self, priority: str) -> Iterable[Task]:
        """Ленивый фильтр по priority"""

        logger.info(f"Применение ленивого фильтра по приоритету: {priority}")
        for task in self._tasks:
            if task.priority == priority:
                yield task

    def filter_by_status(self, status: str) -> Iterable[Task]:
        """Ленивый фильтр по status"""

        logger.info(f"Применение ленивого фильтра по статусу: {status}")
        for task in self._tasks:
            if task.status == status:
                yield task

    def __len__(self) -> int:
        """Возвращает количество задач в очереди"""

        return len(self._tasks)
