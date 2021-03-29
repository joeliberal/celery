from way_3 import sub

rs = sub.delay(5,3)
print(rs.get())

print('Finish')