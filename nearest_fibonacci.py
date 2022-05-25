n=int(input())
temp=n
f=0
s=1
l=[0,1]
while temp:
   sum=f+s
   f=s
   s=sum
   l.append(sum)
   temp-=1
for i in range(n,2*n+1):
    if i in l:
        ff=i
        break
for i in range(n,-1,-1):
    if i in l:
        bf=i
        break
if (n-bf)<(ff-n):
    print(bf)
elif (ff-n)<(n-bf):
    print(ff)
else:
    print(bf,ff)