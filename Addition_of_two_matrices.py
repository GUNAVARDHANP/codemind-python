n=int(input())
a=[]
b=[]
sol=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    b.append(list(map(int,input().split())))
for i in range(len(a)):
    ans=[]
    for j in range(len(a[i])):
        ans.append(a[i][j]+b[i][j])
    sol.append(ans)
for i in sol:
    print(*i)