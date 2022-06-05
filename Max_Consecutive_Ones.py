n=int(input())
l=list(map(int,input().split()))
d=0
for i in range(n):
    c=0
    if l[i]==1:
        for j in range(i,n):
            if l[j]==1:
                c+=1
            else:
                break
    if d<c:
        d=c
print(d)