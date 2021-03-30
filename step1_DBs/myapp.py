from redis_celery import add, divide


'''
add.delay(10,90) #delay(args, args, kwargs:..., kwargs ... )
or
add.apply_async(args=[4,3]) #apply_async(args=[value , ...], kwargs{key:value, ...}, methods)
'''
rs = divide.delay(5,0)
print(rs.get(propagate=False))

rs = add.delay(54,6)
rs.forget() #if set backen we must get() or do forget(), else the code gives error 

print('Finished')
'''
get(timeout=1) --->timeout asyncronize change to synctonize
get(prpagate=False) --->show the error and conyinue run code
'''
