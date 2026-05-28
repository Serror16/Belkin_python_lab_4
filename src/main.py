import time
from src.sources import GeneratorSource, FileTaskSource, ApiTaskSource
from src.receiver import collect_tasks
from src.queue import TaskQueue
from src.runner import AsyncTaskRunner
from src.handlers import HighPriorityHandler, LowPriorityHandler
from src.logger_setup import logger

def main():
    sources = [
        GeneratorSource(),
        FileTaskSource("tasks.txt"),
        ApiTaskSource(),
    ]

    queue = TaskQueue()

    logger.info("Начало заполнения очереди")
    for task in collect_tasks(sources):
        queue.add_task(task)

    print(f"Очередь заполнена. Всего задач на обработку: {len(queue)}")

    high_handler = HighPriorityHandler()
    low_handler = LowPriorityHandler()

    with AsyncTaskRunner() as runner:
        print("[Отправка задач на фоновое выполнение]")
        for task in queue:
            if task.priority in ("high", "critical"):
                runner.submit(task, high_handler)
            else:
                runner.submit(task, low_handler)

        print("(Главный синхронный цикл продолжает работу)")
        for tick in range(4):
            print(f"[Tick {tick}] Основной поток свободен и выполняет другие операции...")
            time.sleep(1)
            
        print("Выход из AsyncTaskRunner, ожидая завершения всех задач...")

    print("Финальные статусы задач в очереди")
    for task in queue:
        print(f"Задача {task.id} ({task.priority}) -> Статус: {task.status}")

if __name__ == "__main__":
    main()