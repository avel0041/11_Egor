f = open('24 (1).txt').readline()
f = f.replace('0', ' .').replace('2', ' .').replace('4', ' .').replace('8', ' .').replace('6', ' .')
f = f.split(' ')[1:]
a = []
k=0
for el in f:
    for i in range(0, len(el)):
        if el[i] == 'W':
            k+=1
        if k==37:
            a.append(i+1)
            break
        if k==36 and i==len(el)-1:
            a.append(i+1)
            break
    k=0
print(max(a))
