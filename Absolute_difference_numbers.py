a,b=map(str,input().split())
b=int(b)
l=list(a)
f=''
s=''
for i in range(b):
    f+=l[i]
for i in range(len(l)-b,len(l)):
    s+=l[i]
f=int(f)
s=int(s)
if f>s:
    print(f-s)
else:
    print(s-f)