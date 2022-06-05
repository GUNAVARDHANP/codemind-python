n=int(input())
l=list(map(int,input().split()))
out=[]
for i in range(n):
    pro=1
    for j in range(n):
        if j!=i:
            pro=pro*(l[j])
    out.append(pro)
print(*out)