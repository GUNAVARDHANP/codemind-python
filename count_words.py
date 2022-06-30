n=input()
x=set('AEIOU')
c=0
n=n.upper()
for i in n.split():
    if i[0] in x:
        if i[len(i)-1] not in x:
            c+=1
print(c)