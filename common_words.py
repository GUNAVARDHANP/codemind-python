a=input().lower().split()
b=input().lower().split()
s=[]
for i in b:
    if i in a:
        s.append(i)
print(*s)