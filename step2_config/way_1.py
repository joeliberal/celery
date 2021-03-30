
'''
for project small
'''
from celery import Celery

app = Celery('way_1')

app.conf.broker_url='redis://localhost:6379'
app.conf.result_backend = 'mongodb://localhost:27017/'
app.conf.task_serializer = 'json' #we have many type serializer,json for save data in database
app.conf.result_serializer = 'json'

@app.task
def sub(x, y):
    return x-y