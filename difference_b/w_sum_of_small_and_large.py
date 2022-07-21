a=input()
c=0
d=0
for i in a.split():
    l=[]
    for j in i:
        l.append(ord(j))
    c+=max(l)
    d+=min(l)
print(max([c,d])-min([c,d]))