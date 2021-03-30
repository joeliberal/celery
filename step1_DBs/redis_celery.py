'''
sudo service redis-server status
sudo service redis-server start/stop
redis-server
ps aux | grep redis ---> for show id active
kill -9 id ---> for kill id active
'''

from celery import Celery

app = Celery('redis_celery',backend='redis://localhost:6379', broker='redis://localhost:6379')

@app.task
def add(x,y):
    return x+y

@app.task
def divide(x,y):
    return x/y
'''
celery --app=tasks wworker --loglevel info

'''