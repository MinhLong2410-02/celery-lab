# celery-lab
# YOU DON'T NEED KAFKA FOR YOUR EVENT QUEUE TASKS

Small project to demo how 2 services were able to communicate via Celery-Redis (same logic but can apply for Celery-RabbitMQ), especially helpful in long running AI-related service.

It's light, easier concept to understand, easier to maintain, works expectionally well with Python.

## Why not Kafka?

Kafka is wayyyyy too heavy, if your system needs to scale to adapt, let's say, over a million users then Kafka is properly a more suitable option but most of the time it is `REALLY UNNECCESARY`.

Also not to mention it is taking too much effort to maintain the pipeline.

> DON'T OVER-ENGINEER