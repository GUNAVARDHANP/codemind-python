n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    l1.append(l[i]*l[i])
print(*sorted(l1))