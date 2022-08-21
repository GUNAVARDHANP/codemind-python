r,c=map(int,input().split())
l=[]
s=0
for i in range(r):
    l1=list(map(int,input().split()))
    l.append(l1)
for i in l:
    if i==sorted(i) or i==sorted(i)[::-1]:
        s+=1
print(s)