a=input().lower()
for i in a:
    if i!=' ' and a.count(i)==1:
        print(i)
        break
else:
    print(-1)