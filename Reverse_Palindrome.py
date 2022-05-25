def rev(n):
    rev=0
    temp=n
    while temp>0:
        rev=rev*10+(temp%10)
        temp//=10
    return rev
def pali(n):
    if rev(n)==n:
        return True
    else:
        return False
n=int(input())
n=n+rev(n)
while(1):
    if pali(n):
        print(n)
        break
    else:
        n=n+rev(n)