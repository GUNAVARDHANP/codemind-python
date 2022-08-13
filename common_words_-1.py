a=input().lower()
b=input().lower()
c=0
for i in a.split():
    if i in b.split():
        c+=1
print(c)