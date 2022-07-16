a=list(input().lower())
b=list(input().lower())
l=[]
for i in a:
    if i not in b and i not in l and i!=' ':
        l.append(i)
for i in b:
    if i not in a and i not in l and i!=' ':
        l.append(i)
print(''.join(sorted(l)))