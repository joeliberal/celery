from celery import Celery, Task
from functools import wraps


app = Celery('app')

class MyTask(Task):

    def __call__(self, *args, **kwargs):
        print('Task starting {0.name} {0.request.id}'.format(self))
        return self.run(*args, **kwargs)

app.config_from_object('celeryconfig')

app.Task = MyTask

def decorator1(func):
    @wraps(func) # for protekted of name tasks unique
    def wrapper(*args, **kwargs):
        print('Starting Decorator 1')
        return (*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func) # for protekted of name tasks unique
    def wrapper(*args, **kwargs):
        print('Starting Decorator 2')
        return (*args, **kwargs)
    return wrapper

@app.task()
@decorator1
@decorator2
def helloworld(x):
    return 'hello world' + x

print(helloworld.__class__.mro())
'''
celery is Total of multy tasks
this Task base in celery is (from celery import Task) this customize for all tasks that we making and for match for a queue
this example ClassBaseTask we is MyTask
the celery ever task must be uinque task
'''