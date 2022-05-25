n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    for j in range(b+1):
        if (j**2)%b==a:
            print(j)
            break
    else:
        print(-1)