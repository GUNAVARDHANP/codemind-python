a,b=map(int,input().split())
l=[]
for i in range(a):
    l.append(list(map(int,input().split())))
s=0
o=0
for i in l:
    for j in i:
        if j%2==0:
            s+=j
        else:
            o+=j
print(s,o)