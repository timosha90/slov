person = {'name': 'Darya', 'age': '31', 'city': 'Minsk'}
print(person['age'])

A = ['X5', 'X6', 'XM']
B = ['Model X', 'Model Y']
d = {'BMW': A, 'Tesla': B}
for mn in d.values():
    print(A[0], A[-1], B[0], B[-1] )


d1 = {"a": 100, "b": 200, "c":300}
d2 = {"a": 300, "b": 200, "d":400}
print(d1["b"] == d2["b"])


d = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
pr = 1
for mn in d.values():
    pr *= mn
print(pr)


K = [1, 2, 3, 4, 5, 6]
M = ['a', 'b', 'c', 'd', 'e', 'f']
d = dict(zip(K, M))
print(d)

a = 'pythonist'
d1 = []
d2 = []
for i in a:
    d1.append(i)
    d2.append(a.count(i))
D = dict(zip(d1, d2))
print(D)
