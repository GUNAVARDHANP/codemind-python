def co(n):
    c=0
    if n==0:
        return 1
    if n<0:
        n=abs(n)
    while n>0:
        c+=1
        n//=10
    return c
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if co(min(l))==co(i):
        c+=1
print(c)