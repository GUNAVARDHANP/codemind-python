a=input()
d=0
vow=['a','e','i','o','u']
b=list(a)
for i in range(len(b)):
    c=0
    if b[i] in vow:
        for j in range(i,len(b)):
            if b[j] in vow:
                c+=1
            else:
                break
    if c>d:
        d=c
print(d)