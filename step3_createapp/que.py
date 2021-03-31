from proj.tasks import add, div, sub, avg

rs = add.delay(34,4)
print(rs.get())

rs = sub.delay(34,4)
print(rs.get())

rs = div.delay(34,4)
print(rs.get())


'''
celery -A proj worker -Q qa,qs,qd,qv -l info   --->create queue
celery -A proj inspect active       --->show tasks active in now
celery -A proj inspect active --help
celery -A proj events --dump  --->monitoring
celery -A proj control enable_events
celery -A proj control disable_events
'''