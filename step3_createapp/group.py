from proj.tasks import add, div, sub, avg
from proj.celery import app
from celery import group, chain, chord


g = group(add.s(i, i) for i in range(10))().get() #for group we must to use signature
print(g)
'''partial
g = group(add.s(i, i)for i in range(10))
print(g(10).get())
'''

#FoG math
ch = chain(add.s(2,4) | add.s(2))
print(ch().get())

ch = chain(add.s(4) | div.s(2))
print(ch(6).get())



ch = chord((add.s(i, i) for i in range(10)), avg.s())
print(ch().get())

ch = (group(add.s(i,i) for i in range(10)) | avg.s() | add.s(2) )
print(ch().get())
