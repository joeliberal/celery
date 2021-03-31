from .celery import app



@app.task(name='sum_of_tow_number')#default name task is name function
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

