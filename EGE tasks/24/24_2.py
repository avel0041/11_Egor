# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.
f = open('24_2.txt').readline()
# k=0
# s=0
# for i in range(0, len(f)-1):
#     if (f[i]=='K' and f[i+1]=='L') or (f[i]=='L' and f[i+1]=='K'):
#         k=0
#     else:
#         k+=1
#         s=max(k, s)
# print(s+1)
# 'DVCSATK LDSAK LDSAU'
f = f.replace('KL', 'K L')
f = f.replace('LK', 'L K')
f = f.split()
# ['dsafsadnu', 'dasfnasd', 'asdbfasdfb']
k = 0
for i in f:
    k=max(len(i), k)
# k = max(f, key=len)
print(k)