def digcnt(n):
    if n==0:
        return 1
    elif n<0:
        temp=n*(-1)
        c=0
        while temp:
            c+=1
            temp//=10
        return c
    else:
        temp=n
        c=0
        while temp:
            c+=1
            temp//=10
        return c
n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n):
    s=digcnt(l[i])
    if s==m:
        c+=1
print(c)