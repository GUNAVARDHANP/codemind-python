n=int(input())
arr=list(map(int,input().split()))
b=list(set(arr))
sum=0
for i in b:
    if i%2!=0:
        sum=sum+i
print(sum)    