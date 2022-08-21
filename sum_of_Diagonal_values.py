r,c=map(int,input().split())
l=[]
for i in range(r):
    l1=list(map(int,input().split()))
    l.append(l1)
s=0
for i in range(r):
    s+=l[i][i]
for i in range(r):
    s+=l[i][r-i-1]
if r%2!=0:
    s-=l[r//2][c//2]
print(s)