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
    print(0)
else:
    b=n
    f=n+1
    while prime(b)==False:
        b-=1
    while prime(f)==False:
        f+=1
    if (f-n)<(n-b):
        print(f-n)
    else:
        print(n-b)