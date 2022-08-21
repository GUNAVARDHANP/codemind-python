r,c=map(int,input().split())
l=[]
s=0
d=0
for i in range(r):
    l1=list(map(int,input().split()))
    l.append(l1)
for i in range(c):
    s=0
    for j in range(r):
        s+=l[j][i]
    d=max(d,s)
print(d)