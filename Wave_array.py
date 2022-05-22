n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(1,n-1):
    if i%2!=0:
        c+=1
        if ((l[i-1]<l[i]) and (l[i+1]<l[i])) or ((l[i-1]>l[i]) and (l[i+1]>l[i])):
            d+=1
if c==d:
    print("yes")
else:
    print("no")