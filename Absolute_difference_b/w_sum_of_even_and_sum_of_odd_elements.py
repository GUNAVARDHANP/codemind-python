n=int(input())
l=list(map(int,input().split()))
e=0
o=0
for i in l:
    if i%2==0:
        e+=i
    else:
        o+=i
if e>o:
    print(e-o)
else:
    print(o-e)