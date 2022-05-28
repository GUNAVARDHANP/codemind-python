n=int(input())
l=list(map(int,input().split()))
c=[]
d=0
for i in range(n):
    if l[i]>d and l.count(l[i])==1:
        d=l[i]
        c.append(l[i])
if len(c)>0:
    print(max(c))
else:
    print(-1)