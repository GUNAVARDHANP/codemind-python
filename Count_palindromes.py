def pali(n):
    n=abs(n)
    temp=n
    rev=0
    while temp:
        rev=rev*10+(temp%10)
        temp//=10
    if rev==n:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if pali(i):
        c+=1
print(c)