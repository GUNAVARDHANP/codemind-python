def rev(n):
    rev=0
    temp=n
    while temp:
        rev=rev*10+(temp%10)
        temp//=10
    return rev
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
r=rev(n)
if prime(n) and prime(r):
    print('circular prime')
elif prime(n) and prime(r)==False:
    print('prime but not a circular prime')
else:
    print('not prime')