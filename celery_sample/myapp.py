from proj.tasks import add, div


rs = add.delay(5,2)
print(rs.get())


rs = div.delay(63,3)
print(rs.get())