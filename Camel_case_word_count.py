a=input()
b=list(a)
c=1
for i in range(1,len(b)):
    if b[i].isupper():
        c+=1
print(c)