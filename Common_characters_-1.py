a=input().lower().split()
s=''
b=a[0]
for i in b:
    for j in a:
        if i not in j:
            break
    else:
        s+=i
if s=='':
    print(-1)
else:
    print(s)