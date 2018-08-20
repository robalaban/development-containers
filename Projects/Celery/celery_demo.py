import random
from celery import Celery
from celery.schedules import crontab

# Celery requires instanciation as app object
app = Celery()

# Using redis.yml docker-compose file, changed default broker
app.conf.broker_url = 'redis://127.0.0.1:6379/0'

# Execute finding_mean every Minute
app.conf.beat_schedule = {
    'find-mean-every-minute': {
        'task': 'celery_demo.find_mean',
        'schedule': crontab(),
        'args': (),
    },
}

@app.task
def add(x, y):
    return x + y

@app.task
def find_mean():
    # Generating sample data
    data = [random.random() for _ in range(30)]
    
    return sum(data) / float(len(data))
