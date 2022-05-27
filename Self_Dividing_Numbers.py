def selfd(n):
    temp=n
    d=0
    pd=0
    while n:
        dev=n%10
        if dev==0:
            return False
        elif temp%dev==0:
            d+=1
        pd+=1
        n//=10
    if d==pd:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if selfd(i):
        print(i,end=' ')