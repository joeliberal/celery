from celery import Celery

app = Celery('way_1')


class Config:
    timezone = 'asia/tehran'
    brocker_url = 'redis://localhost:6379/'

app.config_from_object(Config)
'''
import os
os.environ.setdefault('CELERY_CONFIG_MODULE', 'celeryconfig')
app.config_from_envar('CELERY_CONFIG_MODULE)
'''

@app.task
def sub(x, y):
    return x-y


conf = app.conf.humanize(with_default=False, censored=True)#dont active settings default celery and dont show password 
