from typing import Iterable, cast, Dict, Any
from src.models import Task
from random import randint, choice
import os
from src.logger_setup import logger


class GeneratorSource:
    """Генерирует случайное количество задач"""

    def __init__(self):
        self.source_name = self.__class__.__name__
        logger.debug(f"Инициализация {self.source_name}")

    def get_tasks(self) -> Iterable[Task]:
        """Генерирует от 1 до 10 задач со случайными данными"""
        task_count = randint(1, 10)
        logger.info(f"{self.source_name}: генерация {task_count} задач")

        priorities = ["low", "medium", "high", "critical"]

        for i in range(task_count):
            task = Task(task_id=i, description=f"Сгенерированная задача {i}",priority=choice(priorities))
            logger.debug(f"{self.source_name}: создана задача {task.id}")
            yield task

        logger.debug(f"{self.source_name}: завершена генерация {task_count} задач")


class FileTaskSource:
    """Читает задачи из текстового файла"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.source_name = self.__class__.__name__
        logger.debug(f"Инициализация {self.source_name} с файлом {file_path}")

    def get_tasks(self) -> Iterable[Task]:
        """Читает файл построчно. Каждая строка — это payload для новой задачи"""

        if not os.path.exists(self.file_path):
            logger.error(f"Файл {self.file_path} не найден")
            return

        logger.info(f"{self.source_name}: чтение задач из файла {self.file_path}")
        task_count = 0

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                for index, line in enumerate(f):
                    clean_line = line.strip()
                    if clean_line:
                        # Адаптировано под новую сигнатуру Task (приоритет по умолчанию 'medium')
                        task = Task(task_id=index, description=clean_line)
                        logger.debug(f"{self.source_name}: прочитана задача {task.id}: {clean_line[:30]}...")
                        task_count += 1
                        yield task

            logger.info(f"{self.source_name}: загружено {task_count} задач из файла")

        except IOError as e:
            logger.error(f"{self.source_name}: ошибка чтения файла {self.file_path}: {e}", exc_info=True)
        except Exception as e:
            logger.critical(f"{self.source_name}: неожиданная ошибка: {e}", exc_info=True)


class ApiTaskSource:
    """Имитирует получение задач от внешнего API"""

    def __init__(self):
        self.source_name = self.__class__.__name__
        logger.debug(f"Инициализация {self.source_name}")

    def get_tasks(self) -> Iterable[Task]:
        """Имитирует получение данных от внешнего API в формате JSON"""

        api_response = [
            {"id": 1001, "title": "Отправить отчет", "priority": "high"},
            {"id": 1002, "title": "Проверить почту", "priority": "low"},
            {"id": 1003, "title": "Обновить сервер", "priority": "medium"},
        ]

        logger.info(f"{self.source_name}: получение {len(api_response)} задач из API")

        for item in api_response:
            typed_item = cast(Dict[str, Any], item)
            task = Task(task_id=int(typed_item["id"]), description=typed_item["title"], priority=typed_item["priority"])
            logger.debug(f"{self.source_name}: создана задача {task.id} с приоритетом {task.priority}")
            yield task

        logger.debug(f"{self.source_name}: завершена обработка ответа от API")
