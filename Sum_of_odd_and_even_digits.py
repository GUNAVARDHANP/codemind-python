n=int(input())
l=list(map(int,input().split()))
eve=0
odd=0
for i in range(n):
    if i%2==0:
        eve=eve+l[i]
    else:
        odd=odd+l[i]
if eve==odd:
    print("YES")
else:
    print("NO")