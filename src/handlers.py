from typing import Protocol, runtime_checkable
import asyncio
from src.models import Task
from src.logger_setup import logger

@runtime_checkable
class TaskHandler(Protocol):
    "Контракт для асинхронных обработчиков задач"
    async def handle(self, task: Task) -> None:
        ...

class HighPriorityHandler:
    "Обработчик для задач со статусом 'critical' или 'high'"
    async def handle(self, task: Task) -> None:
        logger.info(f"[HighPriorityHandler] Обработка задачи {task.id}: '{task.description}'")
        
        await asyncio.sleep(1.0)
        
        task.status = "completed"
        logger.info(f"[HighPriorityHandler] Задача {task.id} успешно выполнена.")

class LowPriorityHandler:
    "Обработчик для задач со статусом 'medium' или 'low'"
    async def handle(self, task: Task) -> None:
        logger.info(f"[LowPriorityHandler] Обработка задачи {task.id}: '{task.description}'")
        
        await asyncio.sleep(2.5)

        if task.id == 1002:
            raise RuntimeError(f"Симуляция выброса исключения для теста test_runner_error_handler. Задача: {task.id}")
            
        task.status = "completed"
        logger.info(f"[LowPriorityHandler] Задача {task.id} успешно выполнена.")