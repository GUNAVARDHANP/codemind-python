def digcnt(n):
    c=0
    if n==0:
        return 1
    elif n<0:
       temp=n
       temp=temp*(-1)
       while temp:
           c+=1
           temp//=10
       return c
    else:
        temp=n
        while temp:
            c+=1
            temp//=10
        return c
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    s=digcnt(l[i])
    print(s,end=' ')