r,c=map(int,input().split())
l=[]
s=0
for i in range(r):
    l1=list(map(int,input().split()))
    l.append(l1)
l.remove(l[0])
l.remove(l[-1])
for i in l:
    i.remove(i[0])
    i.remove(i[-1])
for i in range(len(l)):
    l[i]=sum(l[i])
print(sum(l))