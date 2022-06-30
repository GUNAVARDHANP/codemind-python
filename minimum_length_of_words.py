n=input()
l=[]
s=[]
for i in n.split():
    l.append(i)
    x=len(i)
    s.append(x)
print(min(s))