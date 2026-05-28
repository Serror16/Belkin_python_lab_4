from src.sources import GeneratorSource, FileTaskSource, ApiTaskSource
from src.receiver import collect_tasks
from src.queue import TaskQueue
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

    print(f"\nОчередь заполнена. Количество задач: {len(queue)}")

    high_prio_stream = queue.filter_by_priority("high")

    print("\nЗадачи с высоким приоритетом (ленивая обработка):")
    for task in high_prio_stream:
        print(f"-> [HIGH] {task}")

    ready_count = sum(1 for t in queue if t.is_ready)
    print(f"\nЗадач, готовых к выполнению (статус pending): {ready_count}")



if __name__ == "__main__":
    main()
