list = [1, 2, 3, 4]
for i in list:
    print(i)

nl = []
nl.append(1)
nl.append(2)
nl.append(3)
nl.insert(3, 4)
nl.insert(6, 7)
nl.append(5)
nl.extend([6,8])
nl.extend((9,10))
nl.extend([(2,3),(3,4)])
[print(i, end=" ") for i in nl]
print()
nl.remove(1)
print(nl)
nl.pop(10)
print(nl)
nl.pop()
print(nl)
del nl[0]
print(nl)
nl.clear()
print(nl)
del nl
# print(nl)
