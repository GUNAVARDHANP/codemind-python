a=input()
l=a.split()
for i in range(len(l)):
    l[i]=list(l[i])
c=0
for i in l:
    for j in range(len(i)-len(i)//2):
        if (i[j] in 'aeiouAEIOU' and i[len(i)-j-1] not in 'aeiouAEIOU') or (i[j] not in 'aeiouAEIOU' and i[len(i)-j-1] in 'aeiouAEIOU'):
            c+=1
print(c)