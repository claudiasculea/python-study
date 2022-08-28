grades = {'Ana':'B', 'Johnny':'C'}
print(grades['Johnny'])
grades['Victor'] = 'C'
print(grades)
print('Maria' in grades)
del(grades['Ana'])
print(grades)
print(grades.keys())
print(grades.values())