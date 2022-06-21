def rev(n):
    rev=0
    while n:
        rev=rev*10+(n%10)
        n//=10
    return rev
n=int(input())
if n>=0:
    print(rev(n))
else:
    n=n*(-1)
    print(rev(n)*(-1))