import os
import tempfile
from src.protocols import TaskSource
from src.sources import FileTaskSource


def test_file_source_read_tasks():
    """Проверка чтения задач из файла"""

    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as f:
        f.write("Задача 1\nЗадача 2\nЗадача 3\n")
        temp_file = f.name
    try:
        source = FileTaskSource(temp_file)
        tasks = list(source.get_tasks())

        assert len(tasks) == 3
        assert tasks[0].description == "Задача 1"
        assert tasks[1].description == "Задача 2"
        assert tasks[2].description == "Задача 3"
        assert tasks[0].id == 0
        assert tasks[1].id == 1
        assert tasks[2].id == 2
    finally:
        os.unlink(temp_file)

def test_file_source_noexist_file():
    """Проверка обработки несуществующего файла"""

    source = FileTaskSource("noexist_file.txt")
    tasks = list(source.get_tasks())
    assert len(tasks) == 0

def test_file_source_empty_file():
    """Проверка обработки пустого файла"""

    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as f:
        temp_file = f.name

    try:
        source = FileTaskSource(temp_file)
        tasks = list(source.get_tasks())
        assert len(tasks) == 0
    finally:
        os.unlink(temp_file)

def test_file_source_protocol():
    """Проверка, что FileTaskSource реализует протокол TaskSource"""

    source = FileTaskSource("tests.txt")
    assert isinstance(source, TaskSource)
