def do(a):
    l=list(a)
    fl=[]
    c=[]
    d=[]
    for i in range(len(l)):
        if l[i] in 'aeiouAEIOU':
            c.append(i)
            d.append(l[i])
        else:
            fl.append(l[i])
    fl=sorted(fl)
    for i in range(len(c)):
        fl.insert(c[i],d[i])
    return ''.join(fl)
a=input().split()
fl=[]
for i in a:
    fl.append(do(i))
print(' '.join(fl))