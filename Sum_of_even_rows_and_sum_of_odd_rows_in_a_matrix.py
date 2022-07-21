n,m=map(int,input().split())
fl=[]
for i in range(n):
    l=list(map(int,input().split()))
    fl.append(l)
c=0
d=0
for i in range(len(fl)):
    if i%2==0:
        c+=sum(fl[i])
    else:
        d+=sum(fl[i])
print(c,d)