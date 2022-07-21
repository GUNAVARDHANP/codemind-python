a=input().lower()
s=''
for i in a:
    if i!=' ' and a.count(i)==1:
        s+=i
print(''.join(sorted(s)))