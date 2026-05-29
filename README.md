# Лабораторная работа №4

## Введение
В этой лабораторной работе был реализован асинхронный исполнитель, управляющий фоновым потоком, обработчики задач, которые обрабатывают часть задач в зависимости от приоритетности.

## Структура проекта

 <pre>
        BELKIN_PYTHON_LAB_4                                 # Лабораторная работа №4
        │
        ├── src/                                            # Исходный код
        │   ├── __init__.py                                 # Маркер пакета Python
        │   ├── models.py                                   # Модель данных (Task)
        │   ├── protocols.py                                # Протокол TaskSource (контракт)
        │   ├── queue.py                                    # Очередь (TaskQueue)
        │   ├── sources.py                                  # Источники задач (GeneratorSource, FileTaskSource, ApiTaskSource)
        │   ├── receiver.py                                 # Функция collect_tasks для сбора задач
        |   ├── runner.py                                   # Асинхронный исполнитель задач
        |   ├── handlers.py                                 # Асинхронные обработчики задач
        │   ├── logger_setup.py                             # Настройка и фабрика логгера
        │   ├── logging_config.py                           # Конфигурация логирования
        │   ├── main.py                                     # Точка входа, демонстрация работы
        │   └── tasks.txt                                   # Файл с задачами для FileTaskSource
        │
        ├── tests/                                          # Unit-тесты
        │   ├── __init__.py                                 # Маркер пакета тестов
        │   ├── test_api.py                                 # Тесты для ApiTaskSource
        │   ├── test_file.py                                # Тесты для FileTaskSource
        │   ├── test_gener.py                               # Тесты для GeneratorSource
        │   ├── test_extra.py                               # Дополнительные тесты (протоколы, receiver)
        |   ├── test_models.py                              # Тесты для Task
        |   ├── test_queue.py                               # Тесты для TaskQueue
        |   ├── test_queue_async.py                         # Тесты для TaskHandler и AsyncTaskRunner
        │   ├── .coverage                                   # Данные о покрытии кода
        │   └── .coveragerc                                 # Конфигурация coverage.py
        │
        ├── .venv/                                          # Виртуальное окружение Python
        ├── .pytest_cache/                                  # Кэш pytest
        ├── __pycache__/                                    # Кэш Python (байт-код)
        │
        ├── pyproject.toml                                  # Конфигурация проекта и инструментов
        ├── requirements.txt                                # Зависимости проекта
        ├── uv.lock                                         # Lock-файл для uv (менеджер зависимостей)
        ├── .gitignore                                      # Игнорируемые файлы для Git
        ├── .pre-commit-config.yaml                         # Настройка pre-commit хуков
        ├── README.md                                       # Описание проекта, титульник
        ├── shell.log                                       # Лог-файл (создается при запуске)
        └── report.pdf                                      # Отчет по лабораторной работе
</pre>

В папке `tests` лежат тесты для лабораторной работы.



### Запуск тестов
```
pytest tests/ --cov=src --cov-report=term
```
