a=input()
b=input()
b+=a
d=''
c=sorted(b)
for i in range(len(c)):
    d+=c[i]
print(d)