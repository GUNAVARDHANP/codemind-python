n=input()
x=[]
c=0
l=['a','e','i','o','u']
for i in n:
    if i in l:
        x.append(i)
for i in l:
    if i not in x:
        print(i,end=' ')
    else:
        # print('0')
        c+=1
if c==len(l):
    print('0')