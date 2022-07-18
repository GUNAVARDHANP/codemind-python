n=int(input())
l=list(map(int,input().split()))
lm=[]
for i in l:
    if i not in lm:
        lm.append(i)
print(*lm)