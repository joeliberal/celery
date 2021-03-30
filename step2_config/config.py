broker_url = 'redis://localhost:6379'
result_backend = 'mongodb://localhost:27017/'
task_serializer = 'json' #we have many type serializer,json for save data in database
result_serializer = 'json'
accept_content = ['json']
timezone = 'asia/tehran'
enable_utc = True

'''
python -m celeryconfig --->this command in terminal for test and survey for error in my config 
'''