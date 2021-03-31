broker_url = 'redis://localhost:6379' #'amqp://username:password@ip:port//' for rabbitmq
result_backend = 'mongodb://localhost:27017/'
task_serializer = 'json' #we have many type serializer,json for save data in database
result_serializer = 'json'
accept_content = ['json']
timezone = 'asia/tehran'
enable_utc = True
include = ['proj.tasks'] #get path we tasks

task_default_queue = 'qv'

task_routes = {
    'proj.tasks.add':{'queue':'qa'},
    'proj.tasks.div':{'queue':'qd'},
    'proj.tasks.sub':{'queue':'qs'},
    'proj.tasks.avg':{'queue':'qv'},
}#celery -A proj worker -Q qa,qd,qs,qv -l info
'''
python -m celeryconfig --->this command in terminal for test and survey for error in my config 
'''