from traceback import print_last


L = [1, 2, 3]

L.append(4)
print(L)

L.insert(4, 5)
print(L)

L.pop()
print(L)

L.pop(1)
print(L)

s = 'abc'
l1 = list(s)
print(l1)
l2 = ''.join(l1)
print(l2)

l1.reverse()
print(l1)
