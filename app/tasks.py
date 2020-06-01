from celery import Celery
from .config import broker_options

app = Celery('tasks', backend='rpc://', broker='sqs://', broker_transport_options = broker_options)

@app.task
def add(x, y):
    return x + y
