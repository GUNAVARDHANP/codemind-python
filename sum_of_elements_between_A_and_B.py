n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
ll=[]
for i in l:
    if i>=a and i<=b:
        ll.append(i)
if len(ll)==0:
    print(-1)
else:
    print(sum(ll))