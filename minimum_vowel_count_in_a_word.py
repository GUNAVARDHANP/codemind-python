n=input()
a=set('aeiouAEIOU')
c=0
l=[]
for i in n.split():
    c=0
    x=list(i)
    for j in x:
        if j in a:
            c+=1
    l.append(c)
print(min(l))