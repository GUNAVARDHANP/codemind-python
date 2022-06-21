n=int(input())
s=str(n)
d=''
c=0
for i in s:
    if i=='6' and c<1:
        d+='9'
        c+=1
    else:
        d+=i
print(int(d))