for m in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    for i in range(k,0,-1):
        g=s[:i]
        g=g[::-1]
        g+=s[i:]
        s=g
    print(s)