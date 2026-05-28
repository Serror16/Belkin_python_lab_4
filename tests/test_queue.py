import pytest  # type: ignore
from src.queue import TaskQueue
from src.models import Task
import types

@pytest.fixture
def create_queue():
    """Фикстура для создания очереди с тестовыми данными"""

    queue = TaskQueue()
    queue.add_task(Task(1, "Task 1", priority="high", status="pending"))
    queue.add_task(Task(2, "Task 2", priority="low", status="pending"))
    queue.add_task(Task(3, "Task 3", priority="high", status="completed"))
    return queue

def test_queue_len(create_queue):
    """Проверка метода __len__"""
    assert len(create_queue) == 3

def test_queue_iteration_second_time(create_queue):
    """Проверка итерации и возможности повторного обхода"""

    first = [t.id for t in create_queue]
    second = [t.id for t in create_queue]

    assert first == [1, 2, 3]
    assert second == [1, 2, 3]
    assert first == second

def test_filter_by_priority(create_queue):
    """Проверка, что фильтр возвращает генератор, а не готовый список"""

    result = create_queue.filter_by_priority("high")

    assert isinstance(result, types.GeneratorType)

    tasks = list(result)
    assert len(tasks) == 2
    assert all(t.priority == "high" for t in tasks)

def test_filter_by_status(create_queue):
    """Проверка ленивой фильтрации по статусу"""

    result = create_queue.filter_by_status("completed")

    assert isinstance(result, types.GeneratorType)
    tasks = list(result)
    assert len(tasks) == 1
    assert tasks[0].id == 3

def test_add_invalid_task():
    """Проверка защиты от добавления некорректных типов данных"""
    queue = TaskQueue()
    with pytest.raises(TypeError):
        queue.add_task("Тип str, а не Task") # type: ignore
