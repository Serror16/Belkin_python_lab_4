import pytest  # type: ignore
from src.models import Task
from src.handlers import HighPriorityHandler, LowPriorityHandler, TaskHandler
from src.runner import AsyncTaskRunner

def test_handler_protocol():
    "Проверяет, что обработчики соответствуют протоколу TaskHandler"
    high_handler = HighPriorityHandler()
    low_handler = LowPriorityHandler()
    
    assert isinstance(high_handler, TaskHandler)
    assert isinstance(low_handler, TaskHandler)

def test_handler_and_runner():
    "Проверяет работу исполнителя через handler"
    task = Task(task_id=999, description="Тестовая задача", priority="high")
    handler = HighPriorityHandler()

    with AsyncTaskRunner() as runner:
        future = runner.submit(task, handler)
        result = future.result(timeout=3.0) 

    assert task.status == "completed"

def test_runner_error_handler():
    "Проверяет, что при падении задачи исполнитель не падает, а фиксирует failed"
    task = Task(task_id=1002, description="Проверить почту", priority="low")
    handler = LowPriorityHandler()

    with AsyncTaskRunner() as runner:
        future = runner.submit(task, handler)
        try:
            future.result(timeout=4.0)
        except Exception:
            pass

    assert task.status == "failed"