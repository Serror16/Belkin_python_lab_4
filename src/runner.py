import asyncio
import threading
from concurrent.futures import Future
from src.models import Task
from src.handlers import TaskHandler
from src.logger_setup import logger

class AsyncTaskRunner:
    "Асинхронный исполнитель задач, который управляет фоновым потоком с асинхронным event loop."
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(
            target=self._run_loop,
            daemon=True,
        )

    def _run_loop(self) -> None:
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def __enter__(self):
        "Запуск цикла в фоновом event loop"
        logger.info("[Запуск фонового асинхронного event loop]")
        self.thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        "Остановка цикла в фоновом event loop"
        logger.info("[Остановка фонового асинхронного event loop]")
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join()
        logger.info("[Фоновый поток успешно завершен]")

    def submit(self, task: Task, handler: TaskHandler) -> Future:
        "Передает асинхронную задачу на выполнение в фоновый event loop"

        handler_coroutine = handler.handle(task)
        future = asyncio.run_coroutine_threadsafe(handler_coroutine, self.loop)

        future.add_done_callback(lambda f: self._custom_callback(f, task))
        return future

    def _custom_callback(self, future: Future, task: Task) -> None:
        "Централизованный перехватчик результатов выполнения задач"
        try:
            future.result()
            logger.info(f"[Лог] Задача {task.id} завершилась без системных сбоев.")
        except Exception as e:
            task.status = "failed"
            logger.error(f"[Ошибка] Сбой при обработке задачи {task.id}: {e}")