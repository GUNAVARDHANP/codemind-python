n,k,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    l.insert(0,l[-1])
    l.pop()
for i in range(q):
    print(l[int(input())])