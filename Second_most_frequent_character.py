a=input()
f=0
d=0
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c>d:
        d=c
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c>f and c!=d:
        f=c
if f==0:
    print(-1)
else:
    for i in a:
        c=0
        for j in a:
            if i==j:
                c+=1
        if c==f:
            print(i)
            break