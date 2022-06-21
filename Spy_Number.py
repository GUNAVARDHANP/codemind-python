n=int(input())
s=0
m=1
while n:
    s=s+(n%10)
    m=m*(n%10)
    n//=10
if s==m:
    print('Spy Number')
else:
    print('Not Spy Number')