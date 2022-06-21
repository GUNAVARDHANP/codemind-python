l=[0,1]
n=int(input())
for i in range(2,n):
    l.append(l[i-1]+l[i-2])
b=n
f=n+1
while b not in l:
    b-=1
while f not in l:
    f+=1
if (f-n)<(n-b):
    print(f)
elif (n-b)<(f-n):
    print(b)
else:
    print(b,f)