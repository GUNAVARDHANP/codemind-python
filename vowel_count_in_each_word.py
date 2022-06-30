n=input()
a=set('aeiouAEIOU')
c=0
for i in n.split():
    c=0
    x=list(i)
    for j in x:
        if j in a:
            c+=1
    print(c,end=' ')