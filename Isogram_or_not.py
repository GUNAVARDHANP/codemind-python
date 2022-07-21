a=input()
l=[]
for i in a:
    if i!=' ' and a.count(i)==1:
        l.append(i)
if sorted(l)==sorted(a):print(True)
else:print(False)