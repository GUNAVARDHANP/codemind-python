n=int(input())
l=list(map(int,input().split()))
d=0
b=set(l)
l1=list(b)
for i in range(len(l1)):
    c=0
    for j in range(n):
        if l1[i]==l[j]:
            c+=1
    if c>=2:
        d=d+(c//2)
print(d)