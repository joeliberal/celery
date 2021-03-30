'''
sudo service rabbitmq-server stop
sudo service rabbitmq-server start
sudo service rabbitmq-server status
'''
from celery import Celery 

app=Celery('rabbitmq_celery', backend='rpc://', broker='amqp://localhost') #broker='amqp://username:password@ip:port'


@app.task
def add(x,y):
    return x+y

'''
celery --app=tasks_2 worker --loglevel info
'''