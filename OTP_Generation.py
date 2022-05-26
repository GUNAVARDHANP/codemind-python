a=input()
b=''
for i in a:
    if int(i)%2!=0:
        b+=str(int(i)**2)
print(b)