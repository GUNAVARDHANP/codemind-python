def rev(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+(temp%10)
        temp//=10
    return rev
n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(n-1,-1,-1):
    ans=ans*10+l[i]
ans=rev(ans)
ans=ans+1
m=[]
while ans:
    m.append(ans%10)
    ans//=10
print(*(m[::-1]))