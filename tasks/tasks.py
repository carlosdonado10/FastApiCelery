import time

import boto3
from celery import Celery
from celery.result import AsyncResult

from src.run_intelligent import run_intelligent

# broker is the connection string to the queue. Default credentials for local queue guest, guest.
app = Celery('Celery Worker')
app.conf.broker_url = 'sqs://:@queue2:9324/0'

app.conf.broker_transport_options = {
    'queue': {
        'url': "http://queue2:9324/000000000000/dev",
        'region': 'elasticmq',
        'access_key_id': 'x',
        'secret_access_key': 'x',
        'support_fanout': True
    }
 }


@app.task()
def run_intelligent_task(scenario_id: int)-> AsyncResult:
    return run_intelligent()
