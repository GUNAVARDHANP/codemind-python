a=input().lower()
for i in a.split():
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    print(c,end=' ')