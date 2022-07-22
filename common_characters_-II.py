a=input().lower()
b=input().lower()
s=''
for i in a:
    if i in b and i not in s and i!=' ':
        s+=i
print(len(s))