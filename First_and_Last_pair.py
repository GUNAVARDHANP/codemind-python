n=int(input())
l=list(map(int,input().split()))
if n%2==0:
    for i in range(n//2):
        print(l[i],l[n-i-1],end=' ')
else:
    for i in range(n//2):
        print(l[i],l[n-i-1],end=' ')
    print(l[n//2],0)