n=int(input())
p=(2*n)-3
for i in range(n):
    j=n
    while j>n-i-1:
        print(j, end=' ')
        j-=1
    j+=1
    if p>0:
        for k in range(p):
            print(j,end=' ')
        p-=2
    if j>1:
        j=n-i
    else:j=2
    while j<n+1:
        print(j, end=' ')
        j+=1
    print()
p=1
for i in range(n-1, 0, -1):
    j=n
    while j>n-i:
        print(j,end=' ')
        j-=1
    j+=1
    for k in range(p):
        print(j, end=' ')
    p+=2
    while j<n+1:
        print(j, end=' ')
        j+=1
    print()