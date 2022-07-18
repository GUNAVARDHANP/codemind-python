n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ll=[]
for i in a:
    if i in b and i not in ll:
        ll.append(i)
print(*ll)