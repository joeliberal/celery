'''
for project big
'''
from celery import Celery

app = Celery('way_1')

app.config_from_object('celeryconfig')

@app.task
def sub(x, y):
    return x-y
    