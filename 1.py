from itertools import*
t='12 13 15 17 21 26 27 31 34 35 43 45 47 51 53 54 56 57 62 65 67 71 72 74 75 76'
g='kb kp ka kq qk qa qc cq ca cb bc ba br bp bk pb pk pr rp rb ra aq ac ar ab ak'
for p in permutations('aqcrpkb'):
    a=t
    for i in range(1, 8):
        a=a.replace(str(i), p[i-1])
    if set(a.split())==set(g.split()):
        print('1 2 3 4 5 6 7 ')
        print(*p)