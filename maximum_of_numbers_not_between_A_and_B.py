n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
lm=[]
for i in l:
    if i<a or i>b:
        lm.append(i)
if len(lm)==0:
    print(-1)
else:
    print(max(lm))