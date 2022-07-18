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
l=list(map(int,input().split()))
c=0
if (l.index(min(l)))<(l.index(max(l))):
    f=l.index(min(l))
    m=l.index(max(l))
else:
    f=l.index(max(l))
    m=l.index(min(l))
for i in range(f,m+1):
    if prime(l[i]):
        c+=1
print(c)