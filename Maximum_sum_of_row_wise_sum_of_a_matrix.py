r,c=map(int,input().split())
l=[]
d=0
for i in range(r):
    l1=list(map(int,input().split()))
    l.append(l1)
for i in range(r):
    s=0
    for j in range(c):
        s+=l[i][j]
    d=max(d,s)
print(d)