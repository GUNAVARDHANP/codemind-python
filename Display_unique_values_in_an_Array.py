n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(n):
    if l.count(l[i])==1:
        c.append(l[i])
if len(c)>0:
    print(*c)
else:
    print(-1)