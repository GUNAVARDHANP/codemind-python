def go(a):
    l=[]
    d=[]
    c=[]
    for i in a:
        if i.isalnum():
            l.append(i)
        else:
            c.append(a.index(i))
            d.append(i)
    l=sorted(l)
    for i in range(len(c)):
        l.insert(c[i],d[i])
    return ''.join(l)
a=input().split()
l=[]
for i in a:
    l.append(go(i))
print(' '.join(l))