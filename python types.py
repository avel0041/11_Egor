a = 123
# print(a[0])
a = a + 1
a = a * 3


b = '123'
print(b[0])
# b[1] = '7'
b = b + '1'
b = b * 3
if '2' in b:
    print('есть')

c = int(b)
d = str(a)

v = ['1', [2, 3], [1, 2]]
print(len(v))
print(v[2][0])
v[1] = 3
# v = v + 3
v = v + [3, [4, 7], 5]
print(v)
if '2' in v:
    print('есть')
v = [1, 2, 3, 2, 1, 5]

n = {1, 2, 3}
n = set(v)
print(n)
# print(n[0])
if 1 in n:
    print('есть')
