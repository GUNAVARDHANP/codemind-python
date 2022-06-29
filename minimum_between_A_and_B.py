n=int(input())
l=[]
c=0
arr=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        l.append(arr[i])
        c+=1
if c>0:
    print(min(l))
else:
    print('-1')