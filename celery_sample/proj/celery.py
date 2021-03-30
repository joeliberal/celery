#name this file must be celery.py
from __future__ import absolute_import, unicode_literals

from celery import Celery

app = Celery('proj')
app.config_from_object('proj.celery_config')

if __name__=='__main__':
    app.start()
'''
celery - a proj worker -l info #we usesd of include and tasks.py
'''