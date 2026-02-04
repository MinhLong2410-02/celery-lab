import time
from celery_app import app
from logger import get_logger

logger = get_logger("worker.tasks")

@app.task(name="worker.count_task", bind=True)
def count_task(self, user_id: str, n: int = 3) -> dict:
    logger.info("Task started: id=%s user_id=%s n=%s", self.request.id, user_id, n)

    for i in range(n):
        time.sleep(1)
        logger.info("Progress: id=%s user_id=%s step=%s/%s", self.request.id, user_id, i + 1, n)

    return {"user_id": user_id, "slept_seconds": n}
