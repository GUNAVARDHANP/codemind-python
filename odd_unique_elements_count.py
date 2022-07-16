n=int(input())
l=list(map(int,input().split()))
c=0
l=list(set(l))
for i in l:
    if i%2!=0:
        c+=1
print(c)