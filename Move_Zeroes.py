n=int(input())
l=list(map(int,input().split()))
c=0
l1=[]
for i in range(n):
    if l[i]==0:
        c+=1
    else:
        l1.append(l[i])
for i in range(c):
    l1.append(0)
print(*l1)