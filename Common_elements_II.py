n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ll=[]
for i in a:
    if i not in b:
        ll.append(i)
for i in b:
    if i not in a:
        ll.append(i)
print(*ll)