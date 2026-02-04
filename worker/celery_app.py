import os
from celery import Celery

broker = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
backend = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")

app = Celery(
    "worker",
    broker=broker,
    backend=backend,
    include=["tasks"],
)

app.conf.worker_concurrency = int(
    os.getenv("CELERY_CONCURRENCY", 1)
)

app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
