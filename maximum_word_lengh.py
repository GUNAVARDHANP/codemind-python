a=input()
m=a.split()
c=0
for i in range(len(m)):
   l=len(m[i])
   if l>c:
       c=l
print(c)