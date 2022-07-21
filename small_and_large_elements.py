n=input().split()
a=n[0]
b=n[-1]
l=[]
for i in a:
    l.append(ord(i))
print(chr(min(l)),end=' ')
l=[]
for i in b:
    l.append(ord(i))
print(chr(max(l)))