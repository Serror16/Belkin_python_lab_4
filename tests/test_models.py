import pytest # type: ignore
from src.models import Task, TaskInvariantError

def test_task_creation():
    """Тест создания задачи с корректными данными"""
    task = Task(task_id=1, description="Написать тесты", priority="high", status="pending")

    assert task.id == 1
    assert task.description == "Написать тесты"
    assert task.priority == "high"
    assert task.status == "pending"


def test_validated_descriptor():
    """Тест ValidatedChoice для поля status и priority"""
    task = Task(task_id=2, description="Тест дескрипторов")

    task.status = "in_progress"
    assert task.status == "in_progress"

    with pytest.raises(TaskInvariantError) as e:
        task.status = "done"
    assert "Недопустимое значение" in str(e.value)

    with pytest.raises(TaskInvariantError):
        Task(task_id=3, description="Ошибка", priority="super_urgent")


def test_property_description():
    """Тест свойства description"""

    with pytest.raises(TaskInvariantError):
        Task(task_id=4, description="")

    task = Task(task_id=5, description="Описание")

    with pytest.raises(TaskInvariantError):
        task.description = ""


def test_property_is_ready():
    """Проверка свойства is_ready"""
    task = Task(task_id=6, description="Тест готовности")
    assert task.is_ready is True

    task.status = "in_progress"
    assert task.is_ready is False

    with pytest.raises(AttributeError):
        task.is_ready = True # type: ignore


def test_non_data_descriptor_read_only_field():
    """Тест ReadOnlyField"""
    task = Task(task_id=10, description="Тест non-data дескриптора")

    assert task.id == 10
    task.id = 999  # type: ignore
    assert task.id == 999
    assert task._id == 10
    del task.__dict__['id']
    assert task.id == 10
