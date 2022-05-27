def solve(n):
    sum=0
    temp=n
    while temp:
        sum=sum+temp%10
        temp//=10
    return sum
n=int(input())
res=solve(n)
while 1:
    if res<10:
        print(res)
        break
    else:
        res=solve(res)