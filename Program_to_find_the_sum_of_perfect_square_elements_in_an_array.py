n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(n):
    if int(l[i]**0.5)==(l[i]**0.5):
        sum=sum+l[i]
print(sum)