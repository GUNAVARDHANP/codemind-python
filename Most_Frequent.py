n=int(input())
l=list(map(int,input().split()))
d=0
l2=[]
for i in range(n):
    c=l.count(l[i])
    if c>d:
        d=c
for i in range(n):
    if l.count(l[i])==d:
        l2.append(l[i])
s=set(l2)
if len(s)>1:
    print(min(s))
else:
    print(*s)