a=input()
l=[]
for i in 'aeiou':
    if i not in a and i not in l:
        l.append(i)
l=sorted(l)
if len(l)==0:
    print(0)
else:
    print(*l)