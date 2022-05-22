a=input()
b=list(a)
c=0
if b[0]=='0':
    print("Invalid")
else:
    for i in a:
        c+=1
    if c==10:
        print("Valid")
    else:
        print("Invalid")