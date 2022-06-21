def dig(n):
    temp=n
    rev=0
    while temp:
        rev=rev+(temp%10)
        temp//=10
    return rev
n=int(input())
while n>9:
    n=dig(n)
print(n)