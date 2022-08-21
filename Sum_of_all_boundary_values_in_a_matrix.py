r,c=map(int,input().split())
l=[]
for i in range(r):
    l1=list(map(int,input().split()))
    l.append(l1)
s=0
s+=sum(l[0])+sum(l[-1])
l.remove(l[0])
l.remove(l[-1])
for i in l:
    s+=i[0]+i[-1]
print(s)