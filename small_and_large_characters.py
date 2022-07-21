for i in input().split():
    l=[]
    for j in i:
        l.append(ord(j))
    print(chr(min(l)),chr(max(l)),end=' ')