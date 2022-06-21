def prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
n=int(input())
if prime(n):
    c=0
    f=0
    while n:
        d=n%10
        if prime(d):
            c+=1
        f+=1
        n//=10
    if c==f:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')