def dig(n):
    c=0
    if n==0:
        c=1
    if n<0:
        n=abs(n)
    while n>0:
        c+=1
        n//=10
    return c
n=int(input())
l=list(map(int,input().split()))
for i in l:
    # print(i)
    print(dig(i),end=' ')