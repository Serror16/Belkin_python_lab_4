from typing import Iterable
from src.models import Task
from src.protocols import TaskSource
from src.sources import GeneratorSource


def test_generator_source_create_tasks():
    """Тест проверяет, что GeneratorSource действительно создает задачи"""

    source = GeneratorSource()
    tasks = list(source.get_tasks())

    assert len(tasks) > 0
    assert isinstance(tasks[0], Task)


def test_task_source_protocol_with_valid_class():
    """Проверка, что класс с правильным методом распознается как TaskSource"""

    class ValidSource:
        def get_tasks(self) -> Iterable[Task]:
            yield Task(task_id=1, description="test")

    source = ValidSource()
    assert isinstance(source, TaskSource)

    tasks = list(source.get_tasks())
    assert len(tasks) == 1
    assert tasks[0].id == 1

def test_task_source_protocol_with_invalid_class():
    """Проверка, что класс без метода get_tasks не распознается"""

    class InvalidSource:
        def not_get_tasks(self):
            pass

    source = InvalidSource()
    assert not isinstance(source, TaskSource)

def test_task_source_protocol_with_wrong_signature():
    """Проверка, что класс с неправильной сигнатурой не распознается"""

    class WrongSignatureSource:
        def get_tasks(self, extra_parameter):
            yield Task(task_id=1, description="test")

    source = WrongSignatureSource()
    assert isinstance(source, TaskSource)
