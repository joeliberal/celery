'''
for projet medium
'''

from celery import Celery

app = Celery('way_2')

app.conf.update(
    broker_url = 'redis://localhost:6379',
    result_backend = 'mongodb://localhost:27017/',
    task_serializer = 'json', #we have many type serializer,json for save data in database
    result_serializer = 'json',
    accept_content = ['json'],
    timezone = 'asia/tehran',
    enable_utc = True,
)

@app.task
def sub(x, y):
    return x-y
    
