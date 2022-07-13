a=input().split()
for i in range(len(a)):
    if i%2==0:
        a[i]=a[i][::-1]
print(*a)