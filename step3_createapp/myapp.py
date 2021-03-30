from proj.tasks import add, div, sub
from proj.celery import app
from celery import group


'''for show state app'''
res = app.AsyncResult('16d5d64a-28ed-4b6a-97e0-5787b2f335fe')#this id of output  run tasks
print(res.successful())
print(res.failed())
print(res.state)
print(res.id)

func = add.signature((2,18)) #(2, 18) default for task add this add to the end task
#add.s(18) this s not accept to parameter
res = func.delay() # this add to the end
res.forget()

rs = add.delay(5,2)
print(rs.get())


rs = div.delay(63,3)
print(rs.get())

result = sub.apply_async((5,6),queue='celery', countdown=3)
print(result.get())
'''
add.apply_async(args=[5,6], countdown=10) #10 secound delay fro run and asyncrinize change to syncrinize
print(rs.get(timeout=2)) #if more than of 2 secound not response then leave it
print(rs.get(propagate=False)) #if eror was you leave and continue run code

'''