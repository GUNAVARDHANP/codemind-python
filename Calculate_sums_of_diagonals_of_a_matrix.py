n=int(input())
l=[]
s=0
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
for i in range(n):
    for j in range(n):
        if i==j:
            s+=l[i][j]
print('Principal Diagonal:',s,sep='')
s=0
for i in range(n):
    for j in range(n):
        if j==n-i-1:
            s+=l[i][j]
print('Secondary Diagonal:',s,sep='')