from tasks.tasks import app as celery_app
from fastapi import FastAPI
from tasks.tasks import run_intelligent_task

app = FastAPI(name='Sample Celery Workers')

database = []  # Should be a database!


@app.get('/task_ids')
def hello_world():
    return database


@app.post('/run_intelligent')
def run_intelligent():
    t = run_intelligent_task.delay(scenario_id=1)
    database.append(t.id)
    return {'task_id': t.id}


@app.post('/abort_task')
def abort(task_id: str):
    return celery_app.control.revoke(task_id=task_id, terminate=True)

