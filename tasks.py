from celery import Celery
import time

# Before running this, up the message broker( rabbitMQ ) in docker. 
app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    time.sleep(10)
    return x + y