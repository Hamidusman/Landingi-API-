from celery import Celery
import time

app = Celery('task', broker='pyamqp://0.0.0.0:5672',
             backend='rpc://')


@app.task
def waiting():
    time.sleep(10)