a=input()
l=sorted(a.split())
d=0
for i in l:
    if len(i)>d:
        d=len(i)
c=d
for i in l:
    if len(i)<c:
        c=len(i)
fl=[]
while c<=d:
    for i in l:
        if len(i)==c:
            fl.append(i)
    c+=1
print(' '.join(fl))