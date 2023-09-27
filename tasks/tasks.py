import time

from celery import Celery
from celery.result import AsyncResult

from src.run_intelligent import run_intelligent

# broker is the connection string to the queue. Default credentials for local queue guest, guest.
app = Celery('Celery Worker', broker='amqp://guest:guest@queue:5672//')


@app.task()
def run_intelligent_task(scenario_id: int)-> AsyncResult:
    return run_intelligent()
