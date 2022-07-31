a,b=map(int,input().split())
l=[]
for i in range(a):
    l.append(list(map(int,input().split())))
s=[]
for i in l:
    s.append(sum(i))
for j in range(len(l)):
    c=0
    for i in l:
        c+=i[j]
    s.append(c)
print(max(s))