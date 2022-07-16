n=int(input())
l=list(map(int,input().split()))
m=int(input())
l1=[]
for i in l:
    if i not in l1 and l.count(i)==m:
        l1.append(i)
if len(l1)==0:
    print(-1)
else:
    print(*l1)