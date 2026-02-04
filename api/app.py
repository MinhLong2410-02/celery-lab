from flask import Flask, jsonify, request
from celery_client import celery_client

app = Flask(__name__)

@app.post("/jobs")
def create_job():
    payload = request.get_json(silent=True) or {}
    n = int(payload.get("n", 3))
    user_id = payload.get('user_id')
    task = celery_client.send_task("worker.count_task", kwargs={
        "user_id": user_id,
        "n": n
    })

    return jsonify({"task_id": task.id}), 202

@app.get("/jobs/<task_id>")
def job_status(task_id: str):
    res = celery_client.AsyncResult(task_id)
    body = {"task_id": task_id, "state": res.state}

    if res.successful():
        body["result"] = res.result
    elif res.failed():
        body["error"] = str(res.result)

    return jsonify(body), 200
