a=input().lower()
l=[]
for i in a:
    if i!=' ' and i not in l:
        l.append(i)
print(''.join(sorted(l)))