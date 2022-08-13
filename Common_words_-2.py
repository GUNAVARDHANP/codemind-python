c=0
a=input().lower().split()
b=input().lower().split()
for i in a:
    if i in b and a.count(i)==1 and b.count(i)==1:
        c+=1
print(c)