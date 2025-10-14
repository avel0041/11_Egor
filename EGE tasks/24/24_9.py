c=open('24-181.txt').readline()
m=0
for i in range(len(c)):
    for r in range(i+m, len(c)):
        f=c[i:r+1]
        if (f.count('A')+f.count('E')+f.count('I')+f.count('O')+f.count('U')+f.count('Y'))>7 or f.count('.')>=1:
            break
        else:
            m=max(m, len(f))
print(m)


f=open('24-181.txt').readline()
f = f.replace('A', 'Y')
f = f.replace('E', 'Y')
f = f.replace('I', 'Y')
f = f.replace('O', 'Y')
f = f.replace('U', 'Y')
m=0
c1 = 0
c2 = 0
l=0

for i in range(len(f)):
    if f[i]=='Y':
        c1+=1
    if f[i]=='.':
        c2+=1
    while c1>7 or c2>0:
        if f[l]=='Y':
            c1-=1
        if f[l]=='.':
            c2-=1
        l+=1
    m = max(i-l+1, m)
    
print(m)        