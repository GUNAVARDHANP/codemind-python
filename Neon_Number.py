n=int(input())
p=n*n
s=0
while p:
    s+=p%10
    p//=10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")