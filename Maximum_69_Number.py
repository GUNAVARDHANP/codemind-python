s=input()
c=0
for i in s:
    if i=='6' and c<1:
        c+=1
        print(9,end='')
    else:
        print(i,end='')