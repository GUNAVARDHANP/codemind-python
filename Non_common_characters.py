a=input().lower()
b=input().lower()
s=''
for i in a:
    if i not in b and i not in s and i!=' ':
        s+=i
for i in b:
    if i not in a and i not in s and i!=' ':
        s+=i
print(len(s))