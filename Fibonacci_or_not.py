n=int(input())
l=[0,1]
sum=1
s=1
for i in range(2,2*n):
    l.append(sum)
    f=s
    s=sum
    sum=f+s
for i in range(len(l)):
    if l[i]==n:
        print(True)
        break
else:
    print(False)