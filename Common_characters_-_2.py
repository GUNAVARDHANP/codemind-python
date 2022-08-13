a=input().lower().split()
c=0
b=a[0]
for i in b:
    for j in a:
        if i not in j:
            break
    else:
        c+=1
print(c)