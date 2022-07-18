n=int(input())
l=list(map(str,input().split()))
a=[]
b=[]
for i in l:
    a.append(len(i))
for i in range(n):
    if a[i]==max(a):
        b.append(l[i])
print(*b)