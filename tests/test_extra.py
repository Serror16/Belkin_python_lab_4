from src.sources import GeneratorSource
from src.sources import FileTaskSource
from src.sources import ApiTaskSource
from src.receiver import collect_tasks
import tempfile
import os


def test_tasks_from_sources():
    """Проверка сбора задач из нескольких источников"""

    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as f:
        f.write("Файловая задача\n")
        temp_file = f.name

    try:
        sources = [
            GeneratorSource(),
            FileTaskSource(temp_file),
            ApiTaskSource()
        ]

        tasks = list(collect_tasks(sources))
        assert len(tasks) > 0
    finally:
        os.unlink(temp_file)


def test_collect_tasks_empty_list():
    """Проверка с пустым списком источников"""

    tasks = list(collect_tasks([]))
    assert len(tasks) == 0
