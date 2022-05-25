def poe(n):
    for i in range(n+1):
        sq=2**i
        if sq==n:
            return True
    else:
        return False
n=int(input())
if poe(n):
    print(0)
else:
    for i in range(n,-1,-1):
        if poe(i):
            pwr1=i
            break
    for i in range(n,2*n+1):
        if poe(i):
            pwr2=i
            break
    if (n-pwr1)>(pwr2-n):
        print(pwr2-n)
    else:
        print(n-pwr1)