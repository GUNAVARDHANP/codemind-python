a=input()
c=0
l=list(a)
n=len(l)
for i in range(n//2):
    if (l[i] in 'aeiouAEIOU' and l[n-i-1] not in 'aeiouAEIOU' and l[n-i-1]!=' ') or (l[i] not in 'aeiouAEIOU' and l[i]!=' ' and l[n-i-1] in 'aeiouAEIOU'):
        c+=1
print(c)