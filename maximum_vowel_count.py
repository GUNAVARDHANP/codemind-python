a=input().lower()
l=[]
for i in a.split():
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    l.append(c)
print(max(l))