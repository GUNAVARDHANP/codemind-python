r,c=map(int,input().split())
l=[]
for i in range(r):
    l1=list(map(int,input().split()))
    l.append(l1)
for i in range(c):
    s=0
    for j in range(r):
        s+=l[j][i]
    print(s,end=' ')