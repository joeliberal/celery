broker_url = 'redis://localhost:6379' #'amqp://username:password@ip:port//' for rabbitmq
task_serializer = 'json' #we have many type serializer,json for save data in database
result_serializer = 'json'
accept_content = ['json']
timezone = 'asia/tehran'
enable_utc = True
#include = ['tasks',] #get path we tasks
