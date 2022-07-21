for i in input().split():
    l=[]
    for j in i:
        l.append(ord(j))
    print(max(l)-min(l),end=' ')