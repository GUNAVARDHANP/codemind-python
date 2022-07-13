a=list(input())
c=[]
d=[]
r=[]
for i in range(len(a)):
    if a[i].isalpha()==False:
        c.append(i)
        d.append(a[i])
    else:
        r.append(a[i])
r=sorted(r)
for i in range(len(c)):
    r.insert(c[i],d[i])
print(''.join(r))