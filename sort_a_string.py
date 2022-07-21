a=list(input())
l=[]
c=[]
d=[]
for i in range(len(a)):
    if a[i].isalnum():
        l.append(a[i])
    else:
        c.append(i)
        d.append(a[i])
l=sorted(l)
for i in range(len(c)):
    l.insert(c[i],d[i])
print(''.join(l))