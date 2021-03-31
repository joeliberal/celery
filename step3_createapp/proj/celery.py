#name this file must be celery.py

from celery import Celery

app = Celery('proj')
app.config_from_object('proj.celeryconfig')

if __name__=='__main__':
    app.start()

'''
celery - a proj worker -l info #we usesd of include and tasks.py
'''