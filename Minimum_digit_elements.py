def digcount(n):
    temp=n
    c=0
    while temp>0:
        c+=1
        temp//=10
    return c
n=int(input())
l=list(map(int,input().split()))
m=min(l)
co=0
s1=digcount(m)
for i in range(n):
    s=digcount(l[i])
    if s==s1:
        co+=1
print(co)