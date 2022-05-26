a=input()
d=0
b=list(a)
for i in range(len(b)):
    c=0
    if b[i]=='a' or b[i]=='e' or b[i]=='i' or b[i]=='o' or b[i]=='u':
        for j in range(i,len(b)):
            if b[j]=='a' or b[j]=='e' or b[j]=='i' or b[j]=='o' or b[j]=='u':
                c+=1
            else:
                break
        if c>d:
            d=c
print(d)