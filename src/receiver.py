from typing import List, Any, Iterable
from src.protocols import TaskSource
from src.models import Task
from src.logger_setup import logger

def collect_tasks(sources: List[Any]) -> Iterable[Task]:
    """Собирает задачи из всех источников, реализующих контракт TaskSource"""
    logger.info(f"Начало сбора задач из {len(sources)} источников")
    valid_sources = 0
    invalid_sources = 0

    for source in sources:
        if isinstance(source, TaskSource):
            source_name = source.__class__.__name__
            logger.debug(f"Обработка источника: {source_name}")

            try:
                task_count = 0
                for task in source.get_tasks():
                    task_count += 1
                    logger.debug(f"Получена задача {task.id} из {source_name}")
                    yield task

                logger.info(f"Источник {source_name} передал {task_count} задач")
                valid_sources += 1

            except Exception as e:
                logger.error(f"Ошибка при получении задач из {source_name}: {e}", exc_info=True)
        else:
            logger.warning(f"Объект {source} не соответствует контракту TaskSource!")
            invalid_sources += 1

    logger.info(f"Сбор задач завершен. Успешных источников: {valid_sources}, пропущено: {invalid_sources}")
