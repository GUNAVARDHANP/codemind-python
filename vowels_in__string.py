a=input()
l=[]
c=0
for i in a:
    if i in 'AEIOUaeiou' and i not in l:
        l.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(*l)