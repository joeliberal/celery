from __future__ import absolute_import, unicode_literals
from .celery import app

@app.task
def add(x, y):
    return x+y

@app.task
def div(x,y):
    return x/y

@app.task
def sub(x, y):
    return x-y

@app.task
def avg(l):
    return sum(l)/len(l)

