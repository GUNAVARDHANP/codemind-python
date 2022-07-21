a=input()
g=a.split()
a=g[-1]
l=[]
c=122
for i in a:
    if ord(i)<c:
        c=ord(i)
if chr(c).lower() in a:
    print(chr(c).lower())
else:
    print(chr(c))