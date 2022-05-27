def prime(n):
    if n==1 or n==0:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i):
        print(i)