a=input().lower()
l=[]
for i in a:
    if i!=' ' and i not in l:
        l.append(i)
print(len(l))