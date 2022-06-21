n=int(input())
l=[]
for i in range(n):
    l.append(i*(i+1))
if n in l:
    print('YES')
else:
    print('NO')