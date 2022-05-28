n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if l.count(l[i])>n//2:
        print(l[i])
        break