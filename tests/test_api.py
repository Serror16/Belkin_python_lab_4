from src.protocols import TaskSource
from src.sources import ApiTaskSource


def test_api_source_create_tasks():
    """Проверка, что API источник возвращает 3 задачи"""

    source = ApiTaskSource()
    tasks = list(source.get_tasks())

    assert len(tasks) == 3

def test_api_source_task_ids():
    """Проверка ID задач из API"""

    source = ApiTaskSource()
    tasks = list(source.get_tasks())

    assert tasks[0].id == 1001
    assert tasks[1].id == 1002
    assert tasks[2].id == 1003


def test_api_source_protocol():
    """Проверка, что ApiTaskSource реализует протокол TaskSource"""

    source = ApiTaskSource()
    assert isinstance(source, TaskSource)
