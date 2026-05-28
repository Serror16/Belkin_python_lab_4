# Лабораторная работа №3

## Введение
В этой лабораторной работе была создана очередь, поддерживающая итерацию, фильтрацию и потоковую обработку задач. Была добавлена модель TaskQueue и методы: добавления задач в очередь с проверкой на корректность типа(add_task), метод __iter__ для итерации по очереди задач, и два "ленивых" фильтра по статусу и приоритету(filter_by_priority, filter_by_status).

## Структура проекта

 <pre>
        BELKIN_PYTHON_LAB_3                                 # Лабораторная работа №3
        │
        ├── src/                                            # Исходный код
        │   ├── __init__.py                                 # Маркер пакета Python
        │   ├── models.py                                   # Модель данных (Task)
        │   ├── protocols.py                                # Протокол TaskSource (контракт)
        │   ├── queue.py                                    # Очередь (TaskQueue)
        │   ├── sources.py                                  # Источники задач (GeneratorSource, FileTaskSource, ApiTaskSource)
        │   ├── receiver.py                                 # Функция collect_tasks для сбора задач
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
