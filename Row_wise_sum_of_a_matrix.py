r,c=map(int,input().split())
l=[]
for i in range(r):
    l1=list(map(int,input().split()))
    l.append(l1)
for i in range(r):
    s=0
    for j in range(c):
        s+=l[i][j]
    print(s,end=' ')